# Figma to mjml conversion
## Using Python Script

1. Run python file **pyhtonConversionScript.py** to get **finalhtml.html** file containing the layer details in json format.
        
Python command:

	python3 pythonConversionScript.py <File_ID>
	
	Example:
	python3 pythonConversionScript.py Rn8xpFzATy7KbDhOwe9XS1PK
	
    
2. **Json2mjml** tool can change json to mjml and mjml cli tool can change mjml into the responsive html. 

## Output:

1. The Output comes as a **HTML** file named **finalhtml.html**

* Just for the test you can paste json code to the following link:
  
  [Codepen - JSON > MJML > HTML](https://codepen.io/briancsinger/pen/rpYxRJ) 

to get instance output of html.


## Files
* **outputmjml.mjml** contains the mjml tags for the file.
* **finalhtml.html** contains the corresponding html code of the mjml file.


### NOTE:
For the convertion to work, installation of **json2mjml** node package may be required.
1. For installation:

	* npm init
	
	* npm install -g node-modules
	
	* npm i json2mjml
