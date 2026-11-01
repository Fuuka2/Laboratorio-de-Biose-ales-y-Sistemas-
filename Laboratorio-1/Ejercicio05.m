clc;
clear;
close all;

% Intervalo de tiempo
t = -10:0.01:10;

%% x1(t) = u(t)
x1 = double(t >= 0);

%% x2(t) = Pi(t/3)
% Pulso rectangular de ancho 3:
% vale 1 para |t| <= 1.5 y 0 fuera
x2 = double(abs(t) <= 1.5);

%% x3(t)
x3 = zeros(size(t));

% -2 < t < 0
idx1 = (t > -2) & (t < 0);
x3(idx1) = 2 + t(idx1);

% 0 <= t < 5
idx2 = (t >= 0) & (t < 5);
x3(idx2) = 2 - 0.5*t(idx2);

%% x4(t) = 1 - |t|/3, para -3 <= t <= 3
x4 = zeros(size(t));

idx4 = (t >= -3) & (t <= 3);
x4(idx4) = 1 - abs(t(idx4))/3;

%% x5(t) = e^(-2|t|)
x5 = exp(-2*abs(t));

%% x6(t) = sen(6t)/(6t)
% Evitamos división entre cero en t = 0
x6 = ones(size(t));

idx6 = (t ~= 0);
x6(idx6) = sin(6*t(idx6))./(6*t(idx6));


%% GRAFICAS

figure;

subplot(3,2,1)
plot(t,x1,'LineWidth',1.5)
grid on
title('x_1(t) = u(t)')
xlabel('t')
ylabel('x_1(t)')
xlim([-10 10])

subplot(3,2,2)
plot(t,x2,'LineWidth',1.5)
grid on
title('x_2(t) = \Pi(t/3)')
xlabel('t')
ylabel('x_2(t)')
xlim([-10 10])

subplot(3,2,3)
plot(t,x3,'LineWidth',1.5)
grid on
title('x_3(t)')
xlabel('t')
ylabel('x_3(t)')
xlim([-10 10])

subplot(3,2,4)
plot(t,x4,'LineWidth',1.5)
grid on
title('x_4(t) = 1 - |t|/3')
xlabel('t')
ylabel('x_4(t)')
xlim([-10 10])

subplot(3,2,5)
plot(t,x5,'LineWidth',1.5)
grid on
title('x_5(t) = e^{-2|t|}')
xlabel('t')
ylabel('x_5(t)')
xlim([-10 10])

subplot(3,2,6)
plot(t,x6,'LineWidth',1.5)
grid on
title('x_6(t) = sin(6t)/(6t)')
xlabel('t')
ylabel('x_6(t)')
xlim([-10 10])