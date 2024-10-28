R_s = 8  
R_a = 2  
V_a = 10  

def power_delivered_to_speakers(n):
    return (V_a**2 * R_s) / ((n**2 * R_s) + R_a)**2

turns_ratios = [i / 100 for i in range(1, 201)]
powers = [power_delivered_to_speakers(n) for n in turns_ratios]

max_power = max(powers)
optimal_turns_ratio = turns_ratios[powers.index(max_power)]

print(f"The optimal turns ratio is {optimal_turns_ratio:.2f} which delivers a maximum power of {max_power:.2f} watts to the speakers.")
