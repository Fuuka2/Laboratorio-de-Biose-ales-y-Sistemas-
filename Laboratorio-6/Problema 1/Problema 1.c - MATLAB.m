clc; clear; close all;
% Funcion de transferencia
num = [1 0];
den = [1 2 3];
G = tf(num, den);
% Tiempo de simulacion
t = 0:0.01:10;
% Respuesta al impulso
figure;
impulse(G, t);
grid on;
title('Sistema C - Respuesta al Impulso');
xlabel('Tiempo (s)');
ylabel('Amplitud');
% Respuesta al escalon
figure;
step(G, t);
grid on;
title('Sistema C - Respuesta al Escalon');
xlabel('Tiempo (s)');
ylabel('Amplitud');
% Respuesta a la rampa
rampa = t;
[y, tiempo] = lsim(G, rampa, t);
figure;
plot(tiempo, y, 'LineWidth', 1.5);
grid on;
title('Sistema C - Respuesta a la Rampa');
xlabel('Tiempo (s)');
ylabel('Amplitud');
