clc;
clear;
close all;

figure;

T8 = 2*pi;

t8 = 0:0.01:3*T8;

x8 = square((2*pi/T8)*t8,65);

% Convertir de [-1,1] a [0,1]
x8 = (x8 + 1)/2;

subplot(3,2,3)
plot(t8,x8,'LineWidth',1.5);
grid on;
title('Ejercicio 8: Señal cuadrada');
xlabel('Tiempo');
ylabel('Amplitud');
xlim([0 3*T8]);
ylim([-0.2 1.2]);