clc;clear;close all;
% Funcion de transferencia
num = [6];
den = [1 6 5];
G = tf(num, den);
% Tiempo de simulacion
t = 0:0.01:10;
% Respuesta al impulso
figure;
impulse(G, t);
grid on;
title('Sistema A - Respuesta al Impulso');
xlabel('Tiempo (s)');
ylabel('Amplitud');
% Respuesta al escalon
figure;
step(G, t);
grid on;
title('Sistema A - Respuesta al Escalon');
xlabel('Tiempo (s)');
ylabel('Amplitud');
% Respuesta a la rampa
rampa = t;
[y, tiempo] = lsim(G, rampa, t);
figure;
plot(tiempo, y, 'LineWidth', 1.5);
grid on;
title('Sistema A - Respuesta a la Rampa');
xlabel('Tiempo (s)');
ylabel('Amplitud');
