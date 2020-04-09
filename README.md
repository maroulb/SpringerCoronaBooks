# SpringerCoronaBooks

Due to corona crisis [Springer Nature](https://www.springernature.com/gp) is giving away scientific textbooks for [free](https://www.springernature.com/gp/librarians/news-events/all-news-articles/industry-news-initiatives/free-access-to-textbooks-for-institutions-affected-by-coronaviru/17855960).

But getting the books is not straightforward. They provide an [Excel file](https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v4) containing a row for each book with  all relevant information and an 'un-clickable' link to an information page where you can find a download link to the PDF of the book.

If you want to bulk download all books for a specific discipline or even all books for all disciplines you can use the script _spricobo.py_ .


### install dependencies

    pip install -r requirements.txt



### usage

    python spricobo.py [list]

    [list] is a comma separated list (without whitespaces!)
    consisting of abbreviations of disciplines to download:

    all : all books of all disciplines
    bsc : Behavioral Science
    bsp : Behavioral Science and Psychology
    bls : Biomedical and Life Sciences
    bne : Business and Economics
    bnm : Business and Management
    cms : Chemistry and Materials Science
    csc : Computer Science
    ees : Earth and Environmental Science
    enf : Economics and Finance
    edu : Education
    eny : Energy
    eng : Engineering
    hsl : Humanities, Social Sciences and Law
    itr : Intelligent Technologies and Robotics
    lnc : Law and Criminology
    lcm : Literature, Cultural and Media Studies
    mns : Mathematics and Statistics
    med : Medicine
    pna : Physics and Astronomy
    rnp : Religion and Philosophy
    ssc : Social Sciences
