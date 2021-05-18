from tkinter import *
from PIL import Image, ImageTk
# from io import BytesIO
from machineLearning import Rating_prediction, descript_rating_prediction
from word_cloud import make_wordcloud

def plotRating_Predict():
    #Create GUI window, title, and search
    window = Tk()
    searchFrame = Frame()
    window.title("Predict")
    window.minsize(width=400, height=400)
    searchFrame.grid()

    #Title Entry Box
    # titleLabel = Label(searchFrame, text = 'Title:').grid(sticky = E)
    # titleEntry = Entry(searchFrame)
    # titleEntry.grid(row = 0, column = 1, padx = 5, pady= 5)

    #Year Entry box
    yearLabel = Label(searchFrame, text = 'Year:').grid(sticky = E)
    yearEntry = Entry(searchFrame)
    yearEntry.grid(row = 0, column = 1, padx = 20, pady = 5)

    #Duration Entry box
    durationLabel = Label(searchFrame, text = 'Movie Duration (Minute):').grid(sticky = E)
    durationEntry = Entry(searchFrame)
    durationEntry.grid(row = 1, column = 1, padx = 20, pady = 5)

    #num of Genre Entry box
    nrOfGenreLabel = Label(searchFrame, text = 'Number of Genre:').grid(sticky = E)
    nrOfGenreEntry = Entry(searchFrame)
    nrOfGenreEntry.grid(row = 2, column = 1, padx = 20, pady = 5)

    #Genre Entry box
    GenreLabel = Label(searchFrame, text = 'Genre:').grid(sticky = E)
    GenreEntry = Entry(searchFrame)
    GenreEntry.grid(row = 3, column = 1, padx = 20, pady = 5)

    #description Entry box
    desLabel = Label(searchFrame, text = 'Description:').grid(sticky = E)
    desEntry = Entry(searchFrame)
    desEntry.grid(row = 4, column = 1, padx = 20, pady = 5)

    #Get data from entry fields
    waitVariable = IntVar()
    searchButton = Button(searchFrame, text = 'Search and Predict', command = lambda: waitVariable.set(1))
    searchButton.grid(column = 1, padx = 30, pady = 10)
    searchButton.wait_variable(waitVariable)

    # title = titleEntry.get()
    year = yearEntry.get()
    duration = durationEntry.get()
    nrOfGenre = nrOfGenreEntry.get()
    genre = GenreEntry.get()
    descript = desEntry.get()

    #Switch to results
    searchFrame.grid_forget()
    window.title('Movies Rating prediction')
    resultsFrame = Frame()
    resultsFrame.grid()
    resultsFrame.tkraise()


    #Prediction
    predictedRating = Rating_prediction(year,duration,nrOfGenre,genre)
    descript_Rating = descript_rating_prediction(descript)
    #Display Information
    input_info = LabelFrame(resultsFrame, text="Input Information", padx=5, pady=5)
    input_info.grid(row = 1, column = 1,padx = 10, pady = 10, sticky = W)
    input_infoLabel = Label(input_info, text = "Year: " + str(year)).grid(sticky = 'w')
    input_infoLabel = Label(input_info, text = "Duration (Minute): " + str(duration)).grid(sticky = 'w')
    input_infoLabel = Label(input_info, text = "Number of Genre: " + str(nrOfGenre)).grid(sticky = 'w')
    input_infoLabel = Label(input_info, text = "Genre: " + str(genre)).grid(sticky = 'w')

    # input_infoLabel = Label(input_info, text = "description: " + str(descript)).grid(sticky = 'w')

    #Display Predictions
    predictions = LabelFrame(resultsFrame, text="Prediction", padx=5, pady=5)
    predictions.grid(row = 2, column = 1,padx = 10, pady = 20, sticky = W)
    predictionLabel = Label(predictions, text = "Predicted Rating: " + str(predictedRating)).grid(sticky = 'w')
    predictionLabel = Label(predictions, text = "Description Rating: " + str(descript_Rating)).grid(sticky = 'w')

    #Display the wordcloud
    make_wordcloud(descript)
    image = Image.open("img/wordcloud.png")
    word_cloud = ImageTk.PhotoImage(image)
    word_cloudLabel = Label(image=word_cloud)
    word_cloudLabel.image = word_cloud
    word_cloudLabel.grid(row = 0, column = 2, padx = 20)


    #Run the application Again
    restartWaitVar = IntVar()
    restartButton = Button(resultsFrame, text = 'Close', command = lambda: restartWaitVar.set(1))
    restartButton.grid(pady = 10,column = 1)
    restartButton.wait_variable(restartWaitVar)
    restart(window)

    window.mainloop()


def restart(window):
    window.destroy()
    # plotRating_Predict()