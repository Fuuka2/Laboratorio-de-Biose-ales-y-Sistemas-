t = linspace(0, 3, 500);
x = exp(-5 * t);

num_a = [6];
den_a = [1, 6, 5];
sys_a = tf(num_a, den_a);

[h_a, ~] = impulse(sys_a, t);
y_a = lsim(sys_a, x, t);

figure('Position', [100, 100, 700, 800]);

subplot(3, 1, 1);
plot(t, x, 'Color', '#800080', 'LineWidth', 2); 
title('$x(t) = e^{-5t}$', 'Interpreter', 'latex');
ylabel('Amplitud');
xlabel('Tiempo (s)');
grid on;

subplot(3, 1, 2);
plot(t, h_a, 'Color', [0.85, 0.33, 0.1], 'LineWidth', 2);
title({'$H_a(s) = \frac{6}{s^2 + 6s + 5}$', ...
    ' $h_a(t) = \left( \frac{3}{2}e^{-t} - \frac{3}{2}e^{-5t} \right)u(t)$'}, ...
    'Interpreter', 'latex');
ylabel('Amplitud');
xlabel('Tiempo (s)');
grid on;

subplot(3, 1, 3);
plot(t, y_a, 'Color', 'red', 'LineWidth', 2.5);
title('$y_a(t) = h_a(t) * x(t)$', 'Interpreter', 'latex');
xlabel('Tiempo (s)');
ylabel('Amplitud');
grid on;