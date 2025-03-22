/* 001_maksim_football_team_rating.js */ 

function signalerHarcelement(dureeEnSemaines) {
    if (dureeEnSemaines === 1) {
        return "Parle-en aux surveillants.";
    } else if (dureeEnSemaines >= 2 && dureeEnSemaines <= 3) {
        return "Parle-en à ton professeur principal.";
    } else if (dureeEnSemaines >= 6 && dureeEnSemaines <= 8) {
        return "Parle-en au proviseur.";
    } else {
        return "Cherche de l'aide immédiatement auprès d'un adulte de confiance.";
    }
}

// Exemple d'utilisation
const dureeEnSemaines = parseInt(prompt("Depuis combien de semaines subis-tu du harcèlement ? "));
console.log(signalerHarcelement(dureeEnSemaines));


