# Question - Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climb_stairs(n: int) -> int:
    """
    Calculate the number of distinct ways to climb a staircase with n steps,
    where each step you can climb either 1 or 2 steps.

    Args:
        n: The number of steps in the staircase

    Returns:
        The number of distinct ways to climb to the top
    """
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Initialize dp array to store the number of ways to reach each step
    dp = [0] * (n + 1)

    # Base cases
    dp[1] = 1  # 1 way to climb 1 step
    dp[2] = 2  # 2 ways to climb 2 steps: 1+1 or 2

    # Calculate ways for each step
    for i in range(3, n + 1):
        # Number of ways to reach step i = number of ways to reach step (i-1) + number of ways to reach step (i-2)
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# Example usage:
n1 = 2
print(f"Number of ways to climb {n1} stairs: {climb_stairs(n1)}")  # Output: 2

n2 = 3
print(f"Number of ways to climb {n2} stairs: {climb_stairs(n2)}")  # Output: 3

# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimized version with O(1) space complexity
def climb_stairs_optimized(n: int) -> int:
    """
    Optimized solution with O(1) space complexity.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    one_step_before = 2  # Ways to climb 2 steps
    two_steps_before = 1  # Ways to climb 1 step
    all_ways = 0

    for _ in range(3, n + 1):
        all_ways = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = all_ways

    return all_ways

# Example with optimized solution
n3 = 5
print(f"Number of ways to climb {n3} stairs (optimized): {climb_stairs_optimized(n3)}")  # Output: 8