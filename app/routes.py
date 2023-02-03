from flask import Flask, request, render_template
import math
from app import app

# Define endpoint '/' that listens to GET and POST requests


@app.route('/', methods=['GET', 'POST'])
def form():
    # If the request method is GET, render the form
    if request.method == 'GET':
        return render_template('form.html')

    # If the request method is POST, process the form input data
    if request.method == 'POST':
        # Get the values of each input field from the request form
        trailer_size = request.form['trailer-size']
        first_stop_timber = request.form['first-stop-timber']
        first_stop_plastic = request.form['first-stop-plastic']
        second_stop_timber = request.form['second-stop-timber']
        second_stop_plastic = request.form['second-stop-plastic']
        third_stop_timber = request.form['third-stop-timber']
        third_stop_plastic = request.form['third-stop-plastic']
        forth_stop_timber = request.form['forth-stop-timber']
        forth_stop_plastic = request.form['forth-stop-plastic']
        fith_stop_timber = request.form['fith-stop-timber']
        fith_stop_plastic = request.form['fith-stop-plastic']
        sixth_stop_timber = request.form['sixth-stop-timber']
        sixth_stop_plastic = request.form['sixth-stop-plastic']

        # Calculating the total value of all stops' timber and plastic inputs
    result = int(first_stop_timber) + float(first_stop_plastic) + int(second_stop_timber) + float(second_stop_plastic) + int(third_stop_timber) + float(third_stop_plastic) + \
        int(forth_stop_timber) + float(forth_stop_plastic) + int(fith_stop_timber) + \
        float(fith_stop_plastic) + int(sixth_stop_timber) + \
        float(sixth_stop_plastic)

    # Checking if the trailer is full, not full, or over full
    if float(result) == int(trailer_size):
        # If the result is equal to the trailer size, then the trailer is not full
        comment = "Trailer is not full you are not required to consolidate any pallets"
    elif int(result) < int(trailer_size):
        # If the result is less than the trailer size, then the trailer is not full
        comment = "Trailer is not full you are not required to consolidate any pallets"
    else:
        # If the result is greater than the trailer size, then the trailer is full
        comment = "Trailer is full"

    # Calculating the overfull value of the trailer if it exists
    if float(result) > int(trailer_size):
        over = float(result) - int(trailer_size)
    else:
        over = 0

    # Formatting the overfull value to have 2 decimal places
    over = ("{:.2f}".format(over))

    # Converting the overfull value to a float type
    over = float(over)

    # Rounding the overfull value to the nearest quater integer

    def round_to_nearest_quat_int(num):
        return round(num * 4) / 4

    over = round_to_nearest_quat_int(over)

    # Converting the overfull value to a string type
    over = str(over)

    if over == '0.75':
        over_text = "You need to consolidate 1 plastic pallet."
    elif over == '1.0':
        over_text = "You need to consolidate 1 wooden pallet."
    elif over == '1.25':
        over_text = "You need to consolidate 2 plastic pallets."
    elif over == '1.5':
        over_text = "You need to consolidate 2 plastic pallets."
    elif over == '1.75':
        over_text = "You need to consolidate 1 wooden pallet and 1 plastic pallet."
    elif over == '2.0':
        over_text = "You need to consolidate 2 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 plastic pallets."
    elif over == '2.25':
        over_text = "You need to consolidate 1 wooden pallet and 2 plastic pallets."
    elif over == '2.5':
        over_text = "You need to consolidate 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 1 plastic pallet."
    elif over == '2.75':
        over_text = "You need to consolidate 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 1 plastic pallet."
    elif over == '3.0':
        over_text = "You need to consolidate 3 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"1 wooden pallet and 3 plastic pallets."
    elif over == '3.25':
        over_text = "You need to consolidate 5 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 2 plastic pallets."
    elif over == '3.5':
        over_text = "You need to consolidate 2 wooden pallets and 2 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 plastic pallets."
    elif over == '3.75':
        over_text = "You need to consolidate 1 wooden pallet and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 1 plastic pallet."
    elif over == '4.0':
        over_text = "You need to consolidate 6 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 3 plastic pallets."
    elif over == '4.25':
        over_text = "You need to consolidate 1 wooden pallet and 5 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 2 plastic pallets."
    elif over == '4.5':
        over_text = "You need to consolidate 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 1 plastic pallet"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 4 plastic pallets."
    elif over == '4.75':
        over_text = "You need to consolidate 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 1 plastic pallet."
    elif over == '5.0':
        over_text = "You need to consolidate 5 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 3 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"1 wooden pallet and 6 plastic pallets."
    elif over == '5.25':
        over_text = "You need to consolidate 8 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 2 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 5 plastic pallets."
    elif over == '5.5':
        over_text = "You need to consolidate 1 wooden pallet and 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 1 plastic pallet."
    elif over == '5.75':
        over_text = "You need to consolidate 5 wooden pallets and 1 plastic pallet"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"1 wooden pallet and 7 plastic pallets."
    elif over == '6.0':
        over_text = "You need to consolidate 6 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"9 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 3 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 6 plastic pallets."
    elif over == '6.25':
        over_text = "You need to consolidate 1 wooden pallet and 8 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 5 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 2 plastic pallets."
    elif over == '6.5':
        over_text = "You need to consolidate 10 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 1 plastic pallet"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 7 plastic pallets."
    elif over == '6.75':
        over_text = "You need to consolidate 10 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 1 plastic pallet."
    elif over == '7.0':
        over_text = "You need to consolidate 7 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 3 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 6 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"1 wooden pallet and 9 plastic pallets."  
    elif over == '7.25':
        over_text = "You need to consolidate 11 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 2 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 5 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 8 plastic pallets."
    elif over == '7.5':
        over_text = "You need to consolidate 1 wooden pallet and 10 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"7 wooden pallets and 1 plastic pallet"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 7 plastic pallets."
    elif over == '7.75':
        over_text = "You need to consolidate 7 wooden pallets and 1 plastic pallet"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"1 wooden pallet and 10 plastic pallets."
    elif over == '8.0':
        over_text = "You need to consolidate 8 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"12 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 3 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 6 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 9 plastic pallets."
    elif over == '8.25':
        over_text = "You need to consolidate 1 wooden pallet and 11 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 8 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 5 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"7 wooden pallets and 2 plastic pallets."
    elif over == '8.5':
        over_text = "You need to consolidate 13 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 10 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"8 wooden pallets and 1 plastic pallet."
    elif over == '8.75':
        over_text = "You need to consolidate 13 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 10 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"8 wooden pallets and 1 plastic pallet."
    elif over == '9.0':
        over_text = "You need to consolidate 9 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"7 wooden pallets and 3 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 6 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 9 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"1 wooden pallet and 12 plastic pallets."
    elif over == '9.25':
        over_text = "You need to consolidate 14 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 11 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets 8 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 5 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"8 wooden pallets and 2 plastic pallets."
    elif over == '9.5':
        over_text = "You need to consolidate 1 wooden pallet and 13 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 10 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"7 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"9 wooden pallets and 1 plastic pallet."
    elif over == '9.75':
        over_text = "You need to consolidate 1 wooden pallet and 13 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 10 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"7 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"9 wooden pallets and 1 plastic pallet."
    elif over == '10.0':
        over_text = "You need to consolidate 10 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"15 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"8 wooden pallets and 3 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 6 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 9 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 12 plastic pallets."
    elif over == '10.25':
        over_text = "You need to consolidate 1 wooden pallet and 14 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 11 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 8 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"7 wooden pallets and 5 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"9 wooden pallets and 2 plastic pallets."
    elif over == '10.5':
        over_text = "You need to consolidate 16 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 13 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 10 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"8 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"10 wooden pallets and 1 plastic pallet."
    elif over == '10.75':
        over_text = "You need to consolidate 16 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 13 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 10 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"8 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"10 wooden pallets and 1 plastic pallet."
    elif over == '11.0':
        over_text = "You need to consolidate 11 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"9 wooden pallets and 3 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"7 wooden pallets and 6 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 9 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 12 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"1 wooden pallet and 15 plastic pallets."
    elif over == '11.25':
        over_text = "You need to consolidate 17 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 14 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 11 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 8 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"8 wooden pallets and 5 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"10 wooden pallets and 2 plastic pallets."
    elif over == '11.5':
        over_text = "You need to consolidate 1 wooden pallet and 16 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 13 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 10 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"7 wooden pallets and 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"9 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"11 wooden pallets and 1 plastic pallet."
        
    elif over == '11.75':
        over_text = ""
        
    elif over == '12.0':
        over_text = "You need to consolidate 12 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"18 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"10 wooden pallets and 3 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"8 wooden pallets and 6 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 9 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 12 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 15 plastic pallets."
    elif over == '12.25':
        over_text = "You need to consolidate 1 wooden pallet and 17 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 14 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 11 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"7 wooden pallets and 8 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"9 wooden pallets and 5 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"11 wooden pallets and 2 plastic pallets."
    elif over == '12.5':
        over_text = "You need to consolidate 19 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 16 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets 13 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 10 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"8 wooden pallets and 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"10 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"12 wooden pallets and 1 plastic pallet."
        
    elif over == '12.75':
        over_text = ""
        
    elif over == '13.0':
        over_text = "You need to consolidate 13 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"11 wooden pallets and 3 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"9 wooden pallets and 6 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"7 wooden pallets and 9 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallet and 12 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 15 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"1 wooden pallet and 18 plastic pallets."
    elif over == '13.25':
        over_text = "You need to consolidate 20 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"12 wooden pallets and 2 plastic 10 wooden pallets and 5 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"8 wooden pallets and 8 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 11 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 14 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 17 plastic pallets."
    elif over == '13.5':
        over_text = "You need to consolidate 1 wooden pallet and 19 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 16 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 13 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"7 wooden pallets and 10 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"9 wooden pallets and 7 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"11 wooden pallets and 4 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"13 wooden pallets and 1 plastic pallet."
    elif over == '13.75':
        over_text = "You need to consolidate 14 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"21 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"12 wooden pallets and 3 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"10 wooden pallets and 6 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"8 wooden pallets and 9 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 12 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 15 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 18 plastic pallets."
    elif over == '14.0':
        over_text = "You need to consolidate 14 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"21 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"12 wooden pallets and 3 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"10 wooden pallets and 6 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"8 wooden pallets and 9 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 12 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 15 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"2 wooden pallets and 18 plastic pallets."
    elif over == '14.25':
        over_text = "You need to consolidate 1 wooden pallet and 20 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 17 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallets and 14 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"7 wooden pallets and 11 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"9 wooden pallets and 8 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"11 wooden pallets and 5 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"13 wooden pallets and 2 plastic pallets."
        
    elif over == '14.5':
        over_text = ""
        
    elif over == '14.75':
        over_text = ""
        
    elif over == '15.0':
        over_text = "You need to consolidate 15 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"13 wooden pallets and 3 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"11 wooden pallets and 6 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"9 wooden pallets and 9 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"7 wooden pallet and 12 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"5 wooden pallet and 15 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"3 wooden pallets and 18 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"1 wooden pallet and 21 plastic pallets."
    
    elif over == '15.25':
        over_text = ""
        
    elif over == '15.5':
        over_text = ""
        
    elif over == '15.75':
        over_text = ""
        
    elif over == '16.0':
        over_text = "You need to consolidate 16 wooden pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"24 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"14 wooden pallets and 3 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"12 wooden pallets and 6 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"10 wooden pallets and 9 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"8 wooden pallets and 12 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"6 wooden pallets and 15 plastic pallets"+'<br>'+'<br>'+"or"+'<br>'+'<br>'+"4 wooden pallets and 18 plastic pallets 2 wooden pallets and 21 plastic pallets."
    
    else:
        over_text = ''
    # Use the ceil function from the math library to round up the value of "result" to the nearest integer
    result = math.ceil(result)
    
    # Render the 'result.html' template and pass the following variables as arguments to be used in the template: "trailer_size", "result", "comment", "over" and "over_text"
    return render_template('result.html', trailer_size=trailer_size, result=result, comment=comment, over=over, over_text=over_text)

