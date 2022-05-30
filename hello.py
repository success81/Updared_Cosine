#####MAIN WORKING FOR REAL 26MAY######
#####MAIN WORKING FOR REAL 25MAY######
#####MAIN WORKING FOR REAL######
#####MAIN WORKING FOR REAL######
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def home():


    #Libraries
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    import csv
    import re
    import math
    from collections import Counter

    def get_cosine(vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([vec1[x]**2 for x in vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator


    def text_to_vector(text):
        word = re.compile(r'\w+')
        words = word.findall(text)
        return Counter(words)


    def cosine(content_a, content_b):
        text1 = content_a
        text2 = content_b

        vector1 = text_to_vector(text1)
        vector2 = text_to_vector(text2)

        cosine_result = get_cosine(vector1, vector2)
        return cosine_result

    #Importing excel
    filename = "cosine.csv"

    #Setting up lists for csv
    Fields = []
    rows = []

    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
         
        # extracting field names through first row
        fields = next(csvreader)
     
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)



    #Functions
    def cosine_sort_pass(inject_a, my_lib):
        #LIBARIES NECESSARY
        #from nltk.corpus import stopwords
        #from nltk.tokenize import word_tokenize
        #import nltk
        #nltk.download('punkt')
        #nltk.download('stopwords')
        """
        #BASIC COSINE FUNCTION
        def cosine(x, y):
            # tokenization
            X_list = word_tokenize(x) 
            Y_list = word_tokenize(y)
      
            # sw contains the list of stopwords
            sw = stopwords.words('english') 
            l1 =[];l2 =[]
      
            # remove stop words from the string
            X_set = {w for w in X_list if not w in sw} 
            Y_set = {w for w in Y_list if not w in sw}
      
            # form a set containing keywords of both strings 
            rvector = X_set.union(Y_set) 
            for w in rvector:
                if w in X_set: l1.append(1) # create a vector
                else: l1.append(0)
                if w in Y_set: l2.append(1)
                else: l2.append(0)
            c = 0
      
            # cosine formula 
            for i in range(len(rvector)):
                    c+= l1[i]*l2[i]
            #Final variable is cosine
            cosine = c / float((sum(l1)*sum(l2))**0.5)
            return cosine
        """
        my_dict = {}

        for x in my_lib:
            my_pass = cosine(inject_a,x)
            my_dict[x] = my_pass

        sort_cosine = sorted(my_dict.items(), key=lambda x:          x[1],     reverse=True)
       #Portion to return back just the text no numbers
        """
        final_pass = []


        for x in sort_cosine:
            final_pass.append(x[0])
        
        return final_pass
        """
        return sort_cosine

    #Test cases
    test_case = ["Revco", "334118 423430 541512 334111", "Maryland", "Yes", "No", "No", "Yes", "www.cnn.com", "Cybersecurity company that solves cloud security"]
    test_case_b = ["Terala", "334118 345665 334111", "Maryland", "No", "No", "Yes", "Yes", "www.yahoo.com", "Nuclear company providing tough power sources"]
    test_case_c = ["Yara", "334117 429430 541512 334119", "Virginia", "Yes", "Yes", "No", "Yes", "www.tech.com", "World's best cleaning and scrubbing company"]
    #This is the main list of companies if you don't have the CSV files uncomment the line below and delete the other one
    #all_companies = [test_case + test_case_b + test_case_c]

    all_companies = rows

    #Function
    #Counters
    working_list = all_companies#Name Working List
    working_list_naic = []
    pass_list = []
    main_counter = 0
    temp_name = []
    temp_nacic = []
    temp_state = []
    temp_women_owned = []
    temp_disabled_vet = []
    temp_hub_zone = []
    temp_text = []
    temp_eight_a = []
    master_list = []
    temp_list = []
    name_count = 0
    state_count = 0
    nacic_count = 0
    women_owned_count = 0
    eight_a_count = 0
    disabled_vet_count = 0
    hub_zone_count = 0
    text_count = 0
    smart_filter_count = 0


    """""
    #Test Input Areas (Comment out eventually)
    name_input="Yara"
    state_input = "Maryland"
    nacic_input = "334111"
    women_owned_input = "Yes"
    smart_filter_input = "The dog went to the store for cybersecurity and scrubbing and restoring floors"
    text_input = "scrubbing"
    name_count = 0
    nacic_count = 0
    women_owned_count = 0
    state_count = 0
    text_count = 0
    smart_filter_count = 1
    """





    #Instructions
    """
    Here's the plan. We are going to get a talley of the 1 marks. (Name, Naic,State,Women,8A,Hubzone, Vets,Text)  We are going to run through each one. We will  If an analysis ever returns no items. We will add 100 to the counter score. At the end if the counter is over 95(random number). We will return null. If it finishes the entire thing we will return the matching list level to the orginal talley. For example, if it was 4 talleys total I would pull the findngs from the level 4 list.If the total talley is 0 you just return the main list. Smartfilter will look at the completed list and match the free text against that. This was a bad plan. A very bad plan.
    """


    name_input = request.form['a']
    nacic_input = request.form['b']
    state_input = request.form['c']
    women_owned_input = request.form['d']
    eight_a_input = request.form['e']
    disabled_vet_input = request.form['f']
    text_input = request.form['g']
    hub_zone_input = request.form['h']
    smart_filter_input = request.form['i']


    name_count = 0
    nacic_count = 0
    state_count = 0
    women_owned_count = 0
    eight_a_count = 0
    disabled_vet_count = 0
    text_count = 0
    hub_zone_count = 0
    smart_filter_count = 0


    #Name Inputs this determines if the If/else runs
    if name_input != "none":
        name_count += 1
    if nacic_input != "none":
        nacic_count += 1
    if state_input != "none":
        state_count += 1
    if women_owned_input != "none":
        women_owned_count += 1
    if eight_a_input != "none":
        eight_a_count += 1
    if disabled_vet_input != "none":
        disabled_vet_count += 1
    if text_input != "none":
        text_count += 1
    if hub_zone_input != "none":
        hub_zone_count += 1
    if smart_filter_input != "none":
        smart_filter_count += 1


    #talley
    total_talley = name_count + state_count + nacic_count + women_owned_count + eight_a_count + disabled_vet_count + hub_zone_count + text_count






    #Name
    if name_count == 1:
        for x in all_companies:
            if x[0] == name_input:
                    pass_list.append(x[0])
                    pass_list.append(x[1])
                    pass_list.append(x[2])
                    pass_list.append(x[3])
                    pass_list.append(x[4])
                    pass_list.append(x[5])
                    pass_list.append(x[6])
                    pass_list.append(x[7])
                    pass_list.append(x[8])
                    temp_name.append(pass_list)
                    pass_list = []


    #nacic
    if nacic_count == 1:
        for x in all_companies:
            if nacic_input in x[1]:
                pass_list.append(x[0])
                pass_list.append(x[1])
                pass_list.append(x[2])
                pass_list.append(x[3])
                pass_list.append(x[4])
                pass_list.append(x[5])
                pass_list.append(x[6])
                pass_list.append(x[7])
                pass_list.append(x[8])
                temp_nacic.append(pass_list)
                pass_list = []

    #State
    if state_count == 1:
        for x in all_companies:
            if x[2] == state_input:
                    pass_list.append(x[0])
                    pass_list.append(x[1])
                    pass_list.append(x[2])
                    pass_list.append(x[3])
                    pass_list.append(x[4])
                    pass_list.append(x[5])
                    pass_list.append(x[6])
                    pass_list.append(x[7])
                    pass_list.append(x[8])
                    temp_state.append(pass_list)
                    pass_list = []

    #women
    if women_owned_count==1:
        for x in all_companies:
            if x[3] == women_owned_input:
                    pass_list.append(x[0])
                    pass_list.append(x[1])
                    pass_list.append(x[2])
                    pass_list.append(x[3])
                    pass_list.append(x[4])
                    pass_list.append(x[5])
                    pass_list.append(x[6])
                    pass_list.append(x[7])
                    pass_list.append(x[8])
                    temp_women_owned.append(pass_list)
                    pass_list = []

    #eight_a
    if eight_a_count==1:
        for x in all_companies:
            if x[4] == eight_a_input:
                    pass_list.append(x[0])
                    pass_list.append(x[1])
                    pass_list.append(x[2])
                    pass_list.append(x[3])
                    pass_list.append(x[4])
                    pass_list.append(x[5])
                    pass_list.append(x[6])
                    pass_list.append(x[7])
                    pass_list.append(x[8])
                    temp_eight_a.append(pass_list)
                    pass_list = []

    #disabled vet
    if disabled_vet_count==1:
        for x in all_companies:
            if x[5] == disabled_vet_input:
                    pass_list.append(x[0])
                    pass_list.append(x[1])
                    pass_list.append(x[2])
                    pass_list.append(x[3])
                    pass_list.append(x[4])
                    pass_list.append(x[5])
                    pass_list.append(x[6])
                    pass_list.append(x[7])
                    pass_list.append(x[8])
                    temp_disabled_vet.append(pass_list)
                    pass_list = []

    #hub_zone
    if hub_zone_count==1:
        for x in all_companies:
            if x[6] == hub_zone_input:
                    pass_list.append(x[0])
                    pass_list.append(x[1])
                    pass_list.append(x[2])
                    pass_list.append(x[3])
                    pass_list.append(x[4])
                    pass_list.append(x[5])
                    pass_list.append(x[6])
                    pass_list.append(x[7])
                    pass_list.append(x[8])
                    temp_disabled_vet.append(pass_list)
                    pass_list = []

    #Text 
    if text_count == 1:
        for x in all_companies:
            if text_input in x[8]:
                    pass_list.append(x[0])
                    pass_list.append(x[1])
                    pass_list.append(x[2])
                    pass_list.append(x[3])
                    pass_list.append(x[4])
                    pass_list.append(x[5])
                    pass_list.append(x[6])
                    pass_list.append(x[7])
                    pass_list.append(x[8])
                    temp_text.append(pass_list)
                    pass_list = []


    #combining all temp lists into one combined list
    combined_list = temp_name + temp_nacic + temp_state + temp_women_owned + temp_eight_a + temp_disabled_vet + temp_text

    #Taking the name element and putting it in one list
    master_name = []
    for x in combined_list:
        master_name.append(x[0])



    #Dictionary to analyze combined list
    osdbu_dict = {}

    for x in master_name:
        if x in osdbu_dict:
            osdbu_dict[x] += 1
        else:
            osdbu_dict[x] = 1

    #Talley and Dict Analysis
    final_companies = [] #the list of companies in one list
    final_list = [] #the full list with the text field
    final_pass_list = []  #the list the user sees without text

    for k,v in osdbu_dict.items():
        if v == total_talley:
            final_companies.append(k)


    #Pulling final companies from all Companies
    if len(final_companies) > 0:
        for x in all_companies:
            if x[0] in final_companies:
                pass_list.append(x[0])
                pass_list.append(x[1])
                pass_list.append(x[2])
                pass_list.append(x[3])
                pass_list.append(x[4])
                pass_list.append(x[5])
                pass_list.append(x[6])
                pass_list.append(x[7])
                pass_list.append(x[8])
                final_list.append(pass_list)
                pass_list = []

        for x in final_list:
            pass_list.append(x[0])
            pass_list.append(x[1])
            pass_list.append(x[2])
            pass_list.append(x[3])
            pass_list.append(x[4])
            pass_list.append(x[5])
            pass_list.append(x[6])
            pass_list.append(x[7])
            final_pass_list.append(pass_list)
            pass_list = []

    #This is sent if no companies met the combined criteria
    if len(final_companies) == 0 and total_talley > 0:
        final_pass_list = ["No companies found"]

    #If the person put in no search criteria
    if total_talley == 0:
        final_list = all_companies
        for x in final_list:
            pass_list.append(x[0])
            pass_list.append(x[1])
            pass_list.append(x[2])
            pass_list.append(x[3])
            pass_list.append(x[4])
            pass_list.append(x[5])
            pass_list.append(x[6])
            pass_list.append(x[7])
            final_pass_list.append(pass_list)
            pass_list = []
        
            

    #Final variable for output will be final_pass_list 

    #Smart Filter with returns
    if smart_filter_count == 1 and total_talley > 0 and len(final_companies) > 0:
        cosine_list = []
        for x in final_list:
            cosine_list.append(x[8])
            

        cosine_list = cosine_sort_pass(smart_filter_input, cosine_list )

        final_cosine_pass_list = []
        
        for x in cosine_list:
            for ele in final_list:
                if x[0] == ele[8]:
                    pass_list.append(ele[0])
                    pass_list.append(ele[1])
                    pass_list.append(ele[2])
                    pass_list.append(ele[3])
                    pass_list.append(ele[4])
                    pass_list.append(ele[5])
                    pass_list.append(ele[6])
                    pass_list.append(ele[7])
                    pass_list.append(x[1])
                    final_cosine_pass_list.append(pass_list)
                    pass_list = []
        final_pass_list = final_cosine_pass_list

    #Smart Filter without
    if smart_filter_count == 1 and total_talley > 0 and len(final_companies) == 0:
        final_pass_list = "No companies"

    #Smart Filter with no selections
    if smart_filter_count == 1 and total_talley == 0:
        cosine_list = []
        for x in all_companies:
            cosine_list.append(x[8])
            

        cosine_list = cosine_sort_pass(smart_filter_input, cosine_list )

        final_cosine_pass_list = []
        
        for x in cosine_list:
            for ele in final_list:
                if x[0] == ele[8]:
                    pass_list.append(ele[0])
                    pass_list.append(ele[1])
                    pass_list.append(ele[2])
                    pass_list.append(ele[3])
                    pass_list.append(ele[4])
                    pass_list.append(ele[5])
                    pass_list.append(ele[6])
                    pass_list.append(ele[7])
                    pass_list.append(x[1])
                    final_cosine_pass_list.append(pass_list)
                    pass_list = []
        final_pass_list = final_cosine_pass_list






    """"
    print (temp_name)
    print ("break")
    print (temp_nacic)
    print ("break")
    print (temp_state)
    print ("break")
    print (temp_women_owned)
    print ("break")

                




            
    """
    """
    #Name
    if name_count == 0:
        pass
    if name_count == 1:
        if main_counter == 0:
            for x in all_companies:
                if x[0] == name_input:
                    pass_list.append(x[0])
                    pass_list.append(x[1])
                    pass_list.append(x[2])
                    pass_list.append(x[3])
                    pass_list.append(x[4])
                    pass_list.append(x[5])
                    pass_list.append(x[6])
                    pass_list.append(x[7])
                    counter_level_one.append(pass_list)
                    pass_list = []
            main_counter += 1
        if main_counter == 1:
            if len(counter_level_one) == 0:
                pass
            else:
                for x in all_companies:
                    if x[0] == name_input:
                        pass_list.append(x[0])
                        pass_list.append(x[1])
                        pass_list.append(x[2])
                        pass_list.append(x[3])
                        pass_list.append(x[4])
                        pass_list.append(x[5])
                        pass_list.append(x[6])
                        pass_list.append(x[7])
                        counter_level_two.append(pass_list)
                        pass_list = []
                main_counter += 1
                

    print (main_counter)







    #Name Function
    if len(working_list) == 0 and name_count == 1:
        for x in all_companies:
            if x[0] == name_input:
                pass_list.append(x[0])
                pass_list.append(x[1])
                pass_list.append(x[2])
                pass_list.append(x[3])
                pass_list.append(x[4])
                pass_list.append(x[5])
                pass_list.append(x[6])
                pass_list.append(x[7])
                working_list.append(pass_list)
                pass_list = []




    #NAICS FUNCTION
    if len(working_list) == 0 and naic_count == 1:
        for x in all_companies:
            if naic_input in x[1]:
                pass_list.append(x[0])
                pass_list.append(x[1])
                pass_list.append(x[2])
                pass_list.append(x[3])
                pass_list.append(x[4])
                pass_list.append(x[5])
                pass_list.append(x[6])
                pass_list.append(x[7])
                working_list_naic.append(pass_list)
                pass_list = []

    elif len(working_list) >= 1 and naic_count == 1:
        for x in working_list:
            if naic_input in x[1]:
                pass_list.append(x[0])
                pass_list.append(x[1])
                pass_list.append(x[2])
                pass_list.append(x[3])
                pass_list.append(x[4])
                pass_list.append(x[5])
                pass_list.append(x[6])
                pass_list.append(x[7])
                working_list_naic.append(pass_list)
                pass_list = []
    else:
        pass

    print (working_list_naic)
    """
    return render_template('after.html', data = final_pass_list)    


if __name__ == "__main__":
    app.run(debug=True)