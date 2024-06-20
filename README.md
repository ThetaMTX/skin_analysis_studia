## Skin Analysis Application
### Overview
This project is a web application for managing and analyzing skin images. Users can upload, edit, and delete images, as well as view their image gallery. The application requires users to log in, ensuring that only authenticated users can access and manage their images.

### Features
* User Authentication: Users must log in to access the application. Each session requires a new login.
* Image Upload: Users can upload new skin images.
* Image Edit: Users can edit the details of existing images.
* Image Delete: Users can delete images from their gallery.
* Responsive Design: The application features a clean and responsive design for an enhanced user experience.
* Logout Button: A logout button is provided on the image list page for easy user logouts.

### Technologies Used
* Django: Web framework for developing the application.
* HTML/CSS: Frontend technologies for creating the user interface.
* Bootstrap: For responsive design and enhanced UI elements.
* SQLite: Default database for development purposes (can be switched to another database for production).

### Installation
1. Clone the repository:
```
git clone https://github.com/ThetaMTX/skin_analysis_studia.git
cd skin-analysis
```
2. Create a virtual environment and activate it:
```
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Apply migrations:
  ```
python manage.py migrate
```
5. Create a superuser (if needed):
```
python manage.py createsuperuser
``` 
6. Run the development server:
```
python manage.py runserver
```
7. Access the application:
Open your web browser and go to http://127.0.0.1:8000.

### Usage
* Login: Navigate to the login page and log in with your credentials.
* Upload Image: Click on the "Upload New Image" link to upload a new skin image.
* Edit Image: In the image gallery, click on "Edit" under any image to edit its details.
* Delete Image: In the edit image page, click on "Delete Image" to remove the image from your gallery.
* Logout: Click on the "Logout" button at the top-right corner of the image list page to log out.

### Future Plans

# Image Analysis Server
In future updates, we plan to integrate a server that will analyze the uploaded skin images and provide feedback on what the image depicts. This feature aims to assist users in identifying skin conditions or anomalies.

# Steps for Future Integration:
* Set Up Image Analysis Server: Develop or integrate with an existing image analysis server that can process and analyze skin images.
* API Integration: Create API endpoints in the Django application to send images to the analysis server and receive analysis results.
* Display Results: Update the frontend to display analysis results to the user after an image is uploaded or edited.
* Enhance Security: Ensure secure transmission of images and analysis data between the client and server.

### Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.

# License
This project is licensed under the MIT License. See the LICENSE (in a future) file for more details.

# Contact
For questions or suggestions, please open an issue on GitHub or contact the project maintainer at maciejkapan@gmail.com
