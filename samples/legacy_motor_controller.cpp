int readSensor();
void writeMotor(int pwm);

int calculate_pwm(int target, int current) {
    int error = target - current;
    int pwm = error * 3;
    if (pwm > 255) pwm = 255;
    if (pwm < 0) pwm = 0;
    return pwm;
}

void loop() {
    int current = readSensor();
    int pwm = calculate_pwm(100, current);
    writeMotor(pwm);
}
