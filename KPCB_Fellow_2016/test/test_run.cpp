#include <iostream>
#include <fstream>
#include "MyHashMap.h"
#include <string>

int main(int argc, char* argv[]) {
  char* fileName = argv[1];
  
  int cap = 100;
  MyHashMap<int> H(cap);

  std::ifstream inFile(fileName);
  while (true) {
    if (inFile.eof()) break;
    string x;
    inFile >> x;
    if((x.find_first_not_of(' ') == std::string::npos) | (x.empty()))
      continue;
    int y;
    inFile >> y;

    H.set(x, y);
    float temp_load = H.load();
    try {
      if (temp_load > 0.75) {
        throw "Hash map size larger than 75% of the maximum";
      }
    } catch (char* str) {
        std::cout << "Exception: " << str << std::endl;
    }
  }


  std::cout << "Testing load" << std::endl;
  float temp = H.load();
  std::cout << "Load is: " << temp << std::endl;

  std::cout << "Testing get" << std::endl;
  MyHashMap<int>::Iterator v1 = H.get("JJ");
  if (v1 == H.end()) std::cout << "Can not find JJ's record." << std::endl;
  else std::cout << "Mary's value is: " << (*v1).value() << std::endl; 

  std::cout << "Testing remove" << std::endl;
  H.remove("Mary");
  std::cout << "Remove was successful" << std::endl;

  std::cout << "Testing set" << std::endl;
  bool r = H.set("Mary", 100);
  std::cout.setf(std::ios::boolalpha);
  std::cout << "Set result is: " << r << std::endl;


  return 0;
}

    
    
  
