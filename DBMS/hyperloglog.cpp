#include <iostream>
#include <string>
#include "hyperloglog.h"

std::string helloworld()
{
    return "Hello World\n";
}

HyperLogLog::HyperLogLog(int val) : b(val) {}// inititialising initial bits

int HyperLogLog::GetInitialBits()
{
    return b;
}