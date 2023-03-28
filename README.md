# Product Catalogue App

Instructions

--> Added requirements.txt file inside catalogue_project for which installation of various packages are to be done using pip install -r requirements.txt


This project handles 5 cases with 5 different views corresponding to the urls

--> Cases :

  0) Load the products shown in the below excel using any excel reader library (or your own custom reader) of your choice
      
      Here the url for showing all the products from database that was loaded from the given Excel Sheet is : http://localhost:8000/products/
      
   
  1) Given a product name or product code, find the top-most parent of it by its name.
  
     Inorder to access to this , use url http://localhost:8000/faq2/"item_code"/ where item_code is the code of the item for which we need to get its top-most parents's item_name
     
     Example : http://localhost:8000/faq2/AGNES-XL/ ---> this will land you to an html page which answers you the item_name of the top-most parent of AGNES-XL
     
   2) Given a product name, display the name of all of its children in sorted order.
   
      In this case , the url ,  http://localhost:8000/faq3/"item_code"/ will land you to a page that will list out all the item_codes of the child of the item_code , you have provided,
      
      Example : http://localhost:8000/faq3/AGNES/ --->  Will list out all the children of the item_code "AGNES" in ascending order, ie, [AGNES-L ,AGNES-M,AGNES-XS,AGNES-XXL] 
      
   3) Display a count of active and in-active products.
   
      Url --> http://localhost:8000/count/ is to be used to get count of those active and inactive products given as per the sheet.
      
   4)  Display the value of average product price per Category L1 and Category L2
   
       Here we are supposed to be printing the averge values based on both category 1 and category 2.
        
       ie , suppose we have category_l1 with TOP and category_l2 with PANTS , there are numerous records with this combination , so an averge to it will be printed, ie, 115.0000000000000000
       
       Url --> http://localhost:8000/avg/
     
  Note : For better readability , kept all the view functionalities for the above inside a  helpers.py file.
      
