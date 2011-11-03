import string
import sys
import time

#This is a list of the possible inconsistent cross-browser CSS properties, with each version contained in a tuple.
CSS_PROPERTIES = [
        ('box-shadow','-moz-box-shadow','-webkit-box-shadow'),
        ('border-radius','-moz-border-radius','-webkit-border-radius'),
        ('transform','-webkit-transform','-moz-transform','-o-transform','-ms-transform'),
        ('column-count','-webkit-column-count','-moz-column-count'),
        ]
# List of possible inconsistent cross-browser CSS Properties for linear gradients.
CSS_GRADIENT = ['linear-gradient', '-o-linear-gradient', '-moz-linear-gradient', '-webkit-linear-gradient', '-ms-linear-gradient']

def cross_browser_css(filepath):
        f = open(filepath, 'r')                                 # Open the non-cross-browser compatible file
        if not filepath.endswith('.css'):                       # Make sure it's .css!
                print "Not a valid css file."                   # Shame!
                time.sleep(3)
                return False
        lines = f.readlines()                                   # Get the lines from the olf css file
        f.close()                                               # Close the old css file
        backup_path = filepath[:-4]+'-xbrowser.css'
        n = open(backup_path, 'w')                              # Create the cross-browser file
        for line in lines:                                      # Line by line, we go through the css file
                words = line.split(':')                         # splitting the line at the colon
                if len(words) == 2:                             # ignoring lines that contain no colon
                        css_element = words[0].lstrip()                 # separating the css element on the left of the colon
                        css_value = words[1]                            # from the value on the right of it
                        if css_element == 'background-image':           # Check if the css element is a background-image
                                index = words[1].find('gradient')               # Finds the gradient tag after background-image
                                if index != -1:                                 # Check if gradient is used after the background-image
                                        css_element = words[1][:index+8]                # Set css element to the linear-gradient
                                        css_value = words[1][index+8:]                  # Set css value to the data after linear-gradient
                                        for d in CSS_GRADIENT:                          # Go through the CSS Gradient list and
                                                n.write('   background-image: '+d+':'+css_value)        # Write a new line with each CSS gradient property
                        else:
                                for element in CSS_PROPERTIES:          # then checking against our properties list
                                        if css_element in element:              # to see if there's a match. If there is,
                                                for e in element:                       # we go through the tuple containing the variations
                                                        n.write('   '+e+':'+css_value)          # and write out each one, with the given value
                                                break
                                else:
                                         n.write(line.replace('\t','   '))         #If there was no match, we just re-write the line
                else:
                        n.write(line.replace('\t','   '))             #And here we're just rewriting those lines without colons (or with more than one)
        n.close()                                               #Let's close those files up for good measure
        print "Done. Is that all?"
        time.sleep(10)
        
if __name__ == "__main__":                                
        if len(sys.argv) > 0:                                 #If we've taken a file as an argument,
                filepath = sys.argv[1]                            #we run our above method on that file
                cross_browser_css(filepath)
        else:
                print "No file, guy..."
                time.sleep(3)
