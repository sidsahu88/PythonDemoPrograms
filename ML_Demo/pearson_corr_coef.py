# Input Format:
# Physics Scores  15  12  8   8   7   7   7   6   5   3
# History Scores  10  25  17  11  13  17  20  13  9   15
physics_scores = list(map(str, input().split()))
physics_scores = [int(x) for x in physics_scores[2:]]

history_scores = list(map(str, input().split()))
history_scores = [int(x) for x in history_scores[2:]]

n = len(physics_scores)

mean_phys_score = sum(physics_scores) / n
mean_hist_score = sum(history_scores) / n

num = 0
den_x = 0
den_y = 0

for i in range(n):
    x_dev = physics_scores[i] - mean_phys_score
    y_dev = history_scores[i] - mean_hist_score
    
    num += x_dev * y_dev 
    den_x += (x_dev)**2
    den_y += (y_dev)**2

r = num / (den_x * den_y)**0.5

print(f"{r:.3f}")
