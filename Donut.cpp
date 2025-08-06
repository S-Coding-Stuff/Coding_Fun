//
//  Donut.cpp
//  Shapes
//
//

#include "Donut.hpp"
#include <iostream>
#include <cmath>
#include <thread>
#include <chrono>

int screenWidth = 80;
int screenHeight = 24;

const float R1 = 1;
const float R2 = 2;
const float K2 = 10;
const float K1 = 40;
bool colors = true;

const float pi = 3.14159265;

float A = 0;
float B = 0;

float theta_spacing = 0.07;
float phi_spacing = 0.02;

int main() {
    std::cout << "\x1b[2J";
    bool loop = true;
    
    while (loop) {
        std::vector<char> b(screenWidth*screenHeight, ' ');
        std::vector<float> zBuffer(screenWidth*screenHeight, -1e9);
        
        for (float theta=0; theta < 2*pi; theta += theta_spacing){
            for (float phi=0; phi < 2*pi; phi += phi_spacing){
                // x, y, z coordinates for vector
                float x = (R2+R1*cos(theta))*(cos(B)*cos(phi)+sin(A)*sin(B)*sin(phi))-(R1*cos(A)*sin(B)*sin(theta));
                float y = (R2 + R1 * cos(theta)) * (cos(phi) * sin(B) - cos(B) * sin(A) * sin(phi)) + R1 * cos(A) * cos(B) * sin(theta);
                float z = K2 + cos(A) * (R2 + R1 * cos(theta)) * sin(phi) + R1 * sin(A) * sin(theta);
                float ooz = 1/z; // One Over z
                
                // Projection coordinates
                int x_proj = int(screenWidth / 2 + K1 * ooz * x);
                int y_proj = int(screenHeight / 2 - K1 * ooz * y);
                
                float lum = cos(phi) * cos(theta) * sin(B) - cos(A) * cos(theta) * sin(phi) + cos(B) * (cos(A) * sin(theta) - cos(theta) * sin(A) * sin(phi));
                
                if (lum > 0) {
                    int position = x_proj + y_proj * screenWidth;
                    
                    if (position >= 0 && position < screenHeight * screenWidth){
                        if (ooz > zBuffer[position]){
                            zBuffer[position] = ooz;
                            int lumIdx = int(lum*10);
                            if (lumIdx < 0) lumIdx = 0;
                            if (lumIdx > 11) lumIdx = 11;
                            const char lumChars[] = ".,-~:;=!*#$@";
                            b[position] = lumChars[lumIdx > 11 ? 11 :lumIdx];
                        }
                    }
                }
            }
        }
        std::cout << "\x1b[H";
        
        for (int k = 0; k < screenWidth * screenHeight; k++) {
            std::cout << (k % screenWidth ? b[k] : '\n');
        }
        
        A += 0.04;
        B += 0.02;
        std::this_thread::sleep_for(std::chrono::milliseconds(30));
    }
}
