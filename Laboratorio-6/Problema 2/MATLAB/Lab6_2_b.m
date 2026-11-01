t = linspace(0, 1.5, 300); 
x = exp(-5 * t);

num_b = [1, 0, -1];
den_b = [1, -1, 0, -12]; 
sys_b = tf(num_b, den_b);

[h_b, ~] = impulse(sys_b, t);
y_b = lsim(sys_b, x, t);

figure('Position', [100, 100, 700, 800]);

subplot(3, 1, 1);
plot(t, x, 'Color', '#800080', 'LineWidth', 2);
title('$x(t) = e^{-5t}$', 'Interpreter', 'latex');
ylabel('Amplitud');
xlabel('Tiempo (s)');
grid on;

subplot(3, 1, 2);
plot(t, h_b, 'Color', [0.85, 0.33, 0.1], 'LineWidth', 2);
title({'$H_b(s) = \frac{s^2 - 1}{s^3 - s^2 - 12}$', ...
    '$h_b(t) = \left( \frac{4}{5}e^{3t} + \frac{1}{5}e^{-t}\cos(\sqrt{3}t) - \frac{\sqrt{3}}{5}e^{-t}\sin(\sqrt{3}t) \right)u(t)$'}, ...
    'Interpreter', 'latex');
ylabel('Amplitud');
xlabel('Tiempo (s)');
grid on;

subplot(3, 1, 3);
plot(t, y_b, 'Color', 'red', 'LineWidth', 2.5);
title('$y_b(t) = h_b(t) * x(t)$', 'Interpreter', 'latex');
xlabel('Tiempo (s)');
ylabel('Amplitud');
grid on;