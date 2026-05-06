#ifndef  HYPERLOGLOG_H
#define  HYPERLOGLOG_H

#include <string>
// #include <vector>

#define B 

std::string helloworld();

class HyperLogLog {
private:
    int b; //leading bits

public:
    HyperLogLog(int val);

    int GetInitialBits();
    


};

// HyperLogLog(initial_bits);

// int GetCardinality();

// void AddElem(int val);

// int ComputeCardinaliity();

// int computeBinary(hash_t hash);

// int PositionOfLeftmostOne();

// int CalculateHash();

#endif