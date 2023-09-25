import plotly.express as px

# Choosing whether animated or not
while True:
    how = input("How Should the data ne visualized? Should both graphs be shown at the same time or should \nthere "
                "be an animation? Answer either 'animation' or 'on one frame': ")
    if len(how) < 1: quit()  # If user just preses enter without writing anything
    if how.lower() == 'animation' or how.lower() == 'on one frame':
        how = how.lower()  # Deals with capitalization problems
        break
    else: print('Invalid Input... Please try again')

df = px.data.tips()  # Get Dataframe
print('dataframe created...')
print('visualizing...')

# Create main graph based on choice
if how == 'on one frame':
    fig = px.box(df, x='total_bill', y='time', template='plotly_dark', points='all',
                 labels={'time': 'Time', 'total_bill': 'Total Bill'}, color='smoker')
elif how == 'animation':
    fig = px.box(df, x='total_bill', template='plotly_dark', points='all', animation_frame='time', animation_group='total_bill',
                 labels={'time': 'Time', 'total_bill': 'Total Bill'}, notched=True, color='smoker')

# Set same styling for both
fig.update_layout(
    title=dict(text="Total Bill compared to Eating Time and Smoking", font=dict(size=24), automargin=True,
               yref='paper'))
fig.show()
