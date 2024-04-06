class User:
    def __init__(self, id, name, save, saveTotal, mensualSaveEstimated):
        self.id = id
        self.name = name
        self.save = save
        self.saveTotal = saveTotal
        self.mensualSaveEstimated = mensualSaveEstimated

    def save_user(self):
        # Add logic to save the user's data
        pass

    def save_total(self):
        # Add logic to calculate the total savings
        pass

    def estimated_monthly_savings(self):
        # Add logic to estimate the monthly savings
        pass

# Create a User object
user = User(1, "John Doe", 100, 1000, 500)

# Example usage
print(user.name)  # Output: John Doe
print(user.save)  # Output: 100
print(user.saveTotal)  # Output: 1000
print(user.mensualSaveEstimated)  # Output: 500