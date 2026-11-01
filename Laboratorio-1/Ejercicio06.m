clc;
clear;
close all;

figure;
A6 = 2;
T6 = 7;

t6 = 0:0.01:2*T6;
x6 = A6*cos((2*pi/T6)*t6);

subplot(3,2,1)
plot(t6,x6,'LineWidth',1.5);
grid on;
title('Ejercicio 6: Señal cosenoidal');
xlabel('Tiempo (s)');
ylabel('Amplitud');
xlim([0 2*T6]);
ylim([-2.5 2.5]);