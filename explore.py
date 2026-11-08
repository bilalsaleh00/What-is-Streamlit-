import streamlit as st

st.title("Trip Planner")
st.header("Plan Your Trip")

name = st.text_input("What's your name?")

destination = st.selectbox(
    "Choose a destination",
    ["New York", "Los Angeles", "Miami", "Chicago"]
)

days = st.slider(
    "How many days?",
    min_value=1,
    max_value=14,
    value=5
)

budget = st.number_input(
    "Total budget ($)",
    min_value=100,
    value=1000
)

activities = st.multiselect(
    "Choose activities",
    [
        "Sightseeing",
        "Restaurants",
        "Shopping",
        "Museums",
        "Nightlife"
    ]
)

include_hotel = st.checkbox("Include hotel estimate")

st.divider()

# Calculate daily budget
daily_budget = budget / days

# Hotel calculation
if include_hotel:
    hotel_cost = 120 * days
else:
    hotel_cost = 0

remaining_budget = budget - hotel_cost

st.subheader("Trip Summary")

st.write(f"Traveler: **{name or 'Guest'}**")
st.write(f"Destination: **{destination}**")
st.write(f"Trip length: **{days} days**")
st.write(f"Selected activities: **{len(activities)}**")

st.metric(
    "Daily Budget",
    f"${daily_budget:.2f}"
)

if include_hotel:
    st.metric(
        "Estimated Hotel Cost",
        f"${hotel_cost:.2f}"
    )

st.metric(
    "Remaining Budget",
    f"${remaining_budget:.2f}"
)

# Budget message
if daily_budget >= 200:
    st.success("You have a comfortable daily budget!")
elif daily_budget >= 100:
    st.info("Your daily budget looks reasonable.")
else:
    st.warning("Your daily budget may be a little tight.")

# Hotel warning
if remaining_budget < 0:
    st.warning("Your hotel estimate is over your total budget.")

st.divider()

st.subheader("Destination Tip")

if destination == "New York":
    st.info(
        "Budget extra for transportation and attractions."
    )

elif destination == "Los Angeles":
    st.info(
        "Consider transportation costs because the city is spread out."
    )

elif destination == "Miami":
    st.info(
        "Beaches and outdoor activities are popular choices."
    )

elif destination == "Chicago":
    st.info(
        "Museums and downtown attractions are great options."
    )