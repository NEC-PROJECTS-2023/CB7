from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the preprocessed data from CSV file
data = pd.read_csv('preprocessed_data.csv')

@app.route('/')
def index():
    # Get the top trending videos by views and likes
    top_trending_videos = data.nlargest(10, ['views', 'likes'])
    
    # Convert the DataFrame to a list of dictionaries
    trending_videos_list = top_trending_videos.to_dict('records')
    
    # Render the HTML template and pass the trending videos data to it
    return render_template('trending_videos.html', trending_videos=trending_videos_list)

if __name__ == '__main__':
    app.run(debug=True)
