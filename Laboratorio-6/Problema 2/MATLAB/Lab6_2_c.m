t = linspace(0, 3, 500);
x = exp(-5 * t);

num_c = [1, 0];
den_c = [1, 2, 3];
sys_c = tf(num_c, den_c);

[h_c, ~] = impulse(sys_c, t);
y_c = lsim(sys_c, x, t);

figure('Position', [100, 100, 700, 800]);

subplot(3, 1, 1);
plot(t, x, 'Color', '#800080', 'LineWidth', 2);
title('$x(t) = e^{-5t}$', 'Interpreter', 'latex');
ylabel('Amplitud');
xlabel('Tiempo (s)');
grid on;

subplot(3, 1, 2);
plot(t, h_c, 'Color', [0.85, 0.33, 0.1], 'LineWidth', 2);
title({'$H_c(s) = \frac{s}{s^2 + 2s + 3}$', ...
    '$h_c(t) = e^{-t}\left( \cos(\sqrt{2}t) - \frac{1}{\sqrt{2}}\sin(\sqrt{2}t) \right)u(t)$'}, ...
    'Interpreter', 'latex');
ylabel('Amplitud');
xlabel('Tiempo (s)');
grid on;

subplot(3, 1, 3);
plot(t, y_c, 'Color', 'red', 'LineWidth', 2.5);
title('$y_c(t) = h_c(t) * x(t)$', 'Interpreter', 'latex');
xlabel('Tiempo (s)');
ylabel('Amplitud');
grid on;