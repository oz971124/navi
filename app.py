from navi import create_app

# Create App
app = create_app()

# run
if __name__=="__main__":
    app.run(debug=True)