clc;
clear;
close all;

figure;

A7 = 3;
T7 = 5;

t7 = 0:0.01:3*T7;
x7 = A7*sin((2*pi/T7)*t7);

subplot(3,2,2)
plot(t7,x7,'LineWidth',1.5);
grid on;
title('Ejercicio 7: Señal senoidal');
xlabel('Tiempo (s)');
ylabel('Amplitud');
xlim([0 3*T7]);
ylim([-3.5 3.5]);