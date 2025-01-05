import math
import random
import matplotlib.pyplot as plt

def simulated_annealing(initial_temperature, cooling_rate, iterations):
    # Initialize variables
    current_value = random.uniform(0, 100)  # Starting node value
    temperature = initial_temperature
    inferior_node_probabilities = []  # Track probabilities of choosing inferior nodes

    print(f"Initial Value: {current_value:.2f}")
    for i in range(iterations):
        # Generate a new potential value (neighbor node)
        new_value = random.uniform(0, 100)
        
        # Calculate the change in value
        delta = new_value - current_value
        
        if delta < 0:  # Inferior node
            # Calculate the probability of accepting the inferior node
            probability = math.exp(delta / temperature)
            inferior_node_probabilities.append(probability)
            
            # Accept or reject the new node based on probability
            if random.random() < probability:
                current_value = new_value  # Move to the new node
        else:
            # Superior node: Always accept
            current_value = new_value
        
        # Update the temperature
        temperature *= cooling_rate

        # Print progress
        print(f"Iteration {i+1}: Value={current_value:.2f}, Temperature={temperature:.2f}")

    # Return the tracked probabilities for plotting
    return inferior_node_probabilities

# Parameters
initial_temperature = 1000  # Starting temperature
cooling_rate = 0.95         # Cooling rate per iteration
iterations = 50             # Number of iterations

# Run the simulation
probabilities = simulated_annealing(initial_temperature, cooling_rate, iterations)

# Plot the probabilities of accepting inferior nodes
plt.plot(probabilities, marker='o')
plt.title("Effect of Temperature on Probability of Choosing Inferior Nodes")
plt.xlabel("Iteration")
plt.ylabel("Probability")
plt.grid()
plt.show()
