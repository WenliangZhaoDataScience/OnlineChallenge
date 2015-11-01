/*
 * MyHashMap.h: declaration of a Hash Map class
 * Method: Bucket array method with each bucket(linked list) storing keys with same hash code 
 * (low chance), and all bucket is stored in an array. Hash function is from c++ std library. 
 * 
 *  Created on: Oct. 11, 2015
 *      Author: Wenliang Zhao
 */



#include <string>
#include <list>
#include <vector>
using std::string;

// Basic element: entry with K: key, V: value types
template <typename K, typename V>
class Entry {
public:
  Entry(const K& k=K(), const V& v=V())
    : _key(k), _value(v) { }
  const K& key() const { return _key; }
  const V& value() const { return _value; }
  void setKey(const K& k) { _key = k; }
  void setValue(const V& v) { _value = v; }

private:
  K _key;
  V _value;
};

//main class
template <typename V>
class MyHashMap {
public:
  typedef Entry<string, V> Entry1;
  class Iterator;

public:
  MyHashMap(int capacity = 100) : n(0), c(capacity), B(capacity) {}
  int size() const;
  int capa() const;
  bool empty() const;
  float load() const;
  typename MyHashMap<V>::Iterator get(const string& k);
  bool set(const string& k, const V& v);
  void remove(const string& k);
  Iterator begin();
  Iterator end();

protected:
  typedef std::list<Entry1> Bucket;
  typedef std::vector<Bucket> BktArray;
  Iterator find(const string& k);
  Iterator insert(const Iterator& p, const Entry1& e);
  void erase(const Iterator& p);
  typedef typename BktArray::iterator BItor;
  typedef typename Bucket::iterator EItor;
  static void nextEntry(Iterator& p) { ++p.ent; }
  static bool endOfBkt(const Iterator& p) { return p.ent == p.bkt -> end(); }

private:
  int n;              //size of Hash Map
  int c;              // maximum capacity
  BktArray B;         

public:
  std::hash<string> str_hash; 

  class Iterator {
  private:
    EItor ent;
    BItor bkt;
    const BktArray* ba;

  public:
    Iterator(const BktArray& a, const BItor& b, const EItor& q = EItor())
      : ent(q), bkt(b), ba(&a) { }
    Entry1& operator*() const;
    bool operator==(const Iterator& p) const;
    Iterator& operator++();
    friend class MyHashMap;
  };
}; 


// Implementation
template <typename V>
Entry<string, V>& MyHashMap<V>::Iterator::operator*() const { return *ent; }

template <typename V>
bool MyHashMap<V>::Iterator::operator==(const Iterator& p) const {
  if (ba != p.ba || bkt != p.bkt) return false;
  else if (bkt == ba -> end()) return true;
  else return (ent == p.ent);
}

template <typename V>
typename MyHashMap<V>::Iterator& MyHashMap<V>::Iterator::operator++() {
  ++ent;
  if (endOfBkt(*this)) {
    ++bkt;
    while (bkt != ba -> end() && bkt -> empty())
      ++bkt;
    if (bkt == ba -> end()) return *this;
    ent = bkt -> begin();
  }
  return *this;
}

template <typename V>
typename MyHashMap<V>::Iterator MyHashMap<V>::end() { return Iterator(B, B.end()); }

template <typename V>
typename MyHashMap<V>::Iterator MyHashMap<V>::begin() { 
  if (empty()) return end();
  BItor bkt = B.begin();
  while (bkt -> empty()) ++bkt;
  return Iterator(B, bkt, bkt->begin());
}

template <typename V>
int MyHashMap<V>::size() const { return n; }

template <typename V>
int MyHashMap<V>::capa() const { return c; }

template <typename V>
bool MyHashMap<V>::empty() const { return size() == 0; }

template <typename V>
float MyHashMap<V>::load() const {
  return ( (float) size() / (float) capa() );
}


template <typename V>
typename MyHashMap<V>::Iterator MyHashMap<V>::find(const string& k) {
  int i = str_hash(k) % B.size();
  BItor bkt = B.begin() + i;
  Iterator p(B, bkt, bkt->begin());
  while (!endOfBkt(p) && (*p).key() != k)
    nextEntry(p);
  return p;
}

template <typename V>
typename MyHashMap<V>::Iterator MyHashMap<V>::get(const string& k) {
  Iterator p = find(k); 
  if (endOfBkt(p)) {
    return end();
  } else {
    return p;
  }
}


template <typename V>
typename MyHashMap<V>::Iterator MyHashMap<V>::insert(const Iterator& p, const Entry1& e) {
  EItor ins = p.bkt -> insert(p.ent, e);
  n++;
  return Iterator(B, p.bkt, ins);
}


template <typename V>
bool MyHashMap<V>::set(const string& k, const V& v) {
  Iterator p = find(k);
  if (endOfBkt(p)) {
    insert(p, Entry1(k, v));
  }
  else {
    p.ent -> setValue(v);
  }
  Iterator p1 = find(k);
  if (endOfBkt(p1)) return false;
  else  return true;
}


template <typename V>
void MyHashMap<V>::erase(const Iterator& p) {
  p.bkt -> erase(p.ent);
  n--;
}

template <typename V>
void MyHashMap<V>::remove(const string& k) {
  Iterator p = find(k);
  if (endOfBkt(p))
    throw "Erase of nonexistent";
  erase(p);
} 

