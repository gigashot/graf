import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user1_kd = [0.96, 0.95, 0.71, 1.13, 0.70, 0.90, 0.88, 1.34, 1.29, 1.34]
user1_label = "já"
sezony = ['Y6S1', 'Y6S2', 'Y6S3', 'Y6S4', 'Y7S1', 'Y7S2', 'Y7S3', 'Y8S3', 'Y8S4', 'Y9S1']

user2_kd = [0.60, 0.77, 0.91, 0.73, 1.11, 0.88, 0.86, 0.80, 1.0, 0.68]
user2_label = "kamarád"


# graf
plt.figure(figsize=(10, 6))
plt.plot(x, user1_kd, marker='o', color='b', linewidth=2, markersize=5, label=user1_label)
plt.xticks(x, sezony)

plt.plot(x, user2_kd, marker='o', color='r', linewidth=2, markersize=5, label=user2_label)

# osy
plt.xlabel('Sezóny')
plt.ylabel('kd ratio')
#styl
plt.title('Porovnání k/d ratia v R6s')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# legenda
plt.legend(loc='upper left')

# Nastavení rozsahu os y
plt.ylim(0.5, 1.5)

plt.tight_layout()
plt.show()
