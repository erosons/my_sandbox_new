# Simulate data for control and test group over 30 days
np.random.seed(42)

days = pd.date_range(end=datetime.today(), periods=30).to_pydatetime().tolist()

# Assume we have 100 users in each group
users = 100

# Simulating session time (in minutes) for control group (no recommendation engine)
control_session_time = np.random.normal(10, 2, size=(30, users))  # Mean 10 minutes, std deviation 2 minutes

# Simulating session time (in minutes) for test group (with recommendation engine)
test_session_time = np.random.normal(12, 2, size=(30, users))  # Mean 12 minutes (15% increase)

# Simulate Click-Through Rate (CTR) on recommendations for the test group
control_ctr = np.random.uniform(0.05, 0.10, size=(30, users))  # 5% to 10% CTR
test_ctr = np.random.uniform(0.10, 0.20, size=(30, users))  # 10% to 20% CTR (with recommendation)

# Average session time for both groups over 30 days
control_avg_session = control_session_time.mean(axis=1)
test_avg_session = test_session_time.mean(axis=1)

# Average CTR for both groups over 30 days
control_avg_ctr = control_ctr.mean(axis=1)
test_avg_ctr = test_ctr.mean(axis=1)

# Create a DataFrame for comparison
experiment_results = pd.DataFrame({
    'Date': days,
    'Control Avg Session Time (min)': control_avg_session,
    'Test Avg Session Time (min)': test_avg_session,
    'Control Avg CTR': control_avg_ctr,
    'Test Avg CTR': test_avg_ctr
})

import ace_tools as tools; tools.display_dataframe_to_user(name="Experiment Results for User Engagement", dataframe=experiment_results)

# Plotting the Session Time
plt.figure(figsize=(10, 6))
plt.plot(experiment_results['Date'], experiment_results['Control Avg Session Time (min)'], label='Control Group', marker='o', color='blue')
plt.plot(experiment_results['Date'], experiment_results['Test Avg Session Time (min)'], label='Test Group', marker='o', color='green')
plt.title('Average Session Time Over 30 Days')
plt.xlabel('Date')
plt.ylabel('Session Time (min)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Display the plot
plt.show()

# Plotting the CTR
plt.figure(figsize=(10, 6))
plt.plot(experiment_results['Date'], experiment_results['Control Avg CTR'], label='Control Group CTR', marker='o', color='blue')
plt.plot(experiment_results['Date'], experiment_results['Test Avg CTR'], label='Test Group CTR', marker='o', color='green')
plt.title('Click-Through Rate (CTR) Over 30 Days')
plt.xlabel('Date')
plt.ylabel('CTR')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Display the plot
plt.show()
