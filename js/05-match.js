var date = 300;

switch (true) {
    case (date >= 1980 && date <= 2000):
        console.log("Tu eres un milenial");
        break;

    case (date >= 2000 && date <= 2013):
        console.log("Tu eres de la generacion Z, y no de Dragon Ball Z");     
        break;
    
    case (date >= 2014 && date <= 2024):
        console.log("Tu eres un Alpha");
        break;


    case (date != 1980 || (date >= 2000 && date <= 2013) || (date >= 2014 && date <= 2024)):
        console.log("Sos marciano");
        break;
}
