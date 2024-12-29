import streamlit as st

def main():
    st.title("Power Calculation App")

    # User selects type of power calculation
    power_type = st.radio(
        "Select the type of power calculation:",
        ("DC Power", "Single-Phase Power", "Two-Phase Power", "Three-Phase Power")
    )

    if power_type == "DC Power":
        st.header("DC Power Calculation")
        voltage = st.number_input("Enter DC Voltage (V):", min_value=0.0, step=0.1)
        current = st.number_input("Enter DC Current (I):", min_value=0.0, step=0.1)
        if st.button("Calculate DC Power"):
            power = voltage * current
            st.success(f"DC Power (P) = {power} W")

    elif power_type == "Single-Phase Power":
        st.header("Single-Phase Power Calculation")
        voltage = st.number_input("Enter AC Voltage (V):", min_value=0.0, step=0.1)
        current = st.number_input("Enter AC Current (I):", min_value=0.0, step=0.1)
        power_factor = 0.9
        if st.button("Calculate Single-Phase Power"):
            power = voltage * current * power_factor
            st.success(f"Single-Phase Power (P) = {power} W")

    elif power_type == "Two-Phase Power":
        st.header("Two-Phase Power Calculation")
        voltage = st.number_input("Enter AC Voltage (V):", min_value=0.0, step=0.1)
        current = st.number_input("Enter AC Current (I):", min_value=0.0, step=0.1)
        power_factor = 0.9
        if st.button("Calculate Two-Phase Power"):
            power = 2 * voltage * current * power_factor
            st.success(f"Two-Phase Power (P) = {power} W")

    elif power_type == "Three-Phase Power":
        st.header("Three-Phase Power Calculation")
        voltage = st.number_input("Enter AC Voltage (V):", min_value=0.0, step=0.1)
        current = st.number_input("Enter AC Current (I):", min_value=0.0, step=0.1)
        power_factor = 0.9
        if st.button("Calculate Three-Phase Power"):
            power = (3 ** 0.5) * voltage * current * power_factor
            st.success(f"Three-Phase Power (P) = {power} W")

if __name__ == "__main__":
    main()
