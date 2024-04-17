console.log('Juste pour tester ');
if (localStorage.getItem('panier') == null ){
    var panier = {} ; 

}else{
    panier = JSON.parse(localStorage.getItem('panier'));
}
$(document).on('click', '.tedd' , function(){
    console.log('ajouter');
    var item_id = this.id.toString();
    console.log(item_id) ;
    if (panier[item_id] != undefined) {
        quantité = panier[item_id][0]+1 ;
        panier[item_id][0] = quantité ; 
        panier[item_id][2] += parseFloat(document.getElementById("prixunitaire"+item_id).innerHTML);
        

    }else{
        quantité = 1;
        prix = parseFloat(document.getElementById("prixunitaire"+item_id).innerHTML);
        nom = document.getElementById("aaa"+item_id).innerHTML  ;
        panier[item_id] = [quantité , nom, prix] ;
    }
    console.log(panier);
    localStorage.setItem('panier' , JSON.stringify(panier));
    document.getElementById("panier").innerHTML = "Panier(" + Object.keys(panier).length+")" ;
    console.log(Object.keys(panier).length);
});
AfficherList(panier)

function AfficherList(panier) {
    var panierString = "";
    panierString += "<h5> Voici votre liste </h5>";
    var index = 1;
    for (var x in panier) {
        panierString += index;
        var element = document.getElementById("aaa" + x);
        if (element) { // Vérification si l'élément existe
            panierString += element.innerHTML + " Qte " + panier[x][0] + "<br>";
        }
        index += 1;
    }
    panierString += "<a href='/checkout' class='btn btn-primary'>Checkout</a>";
    $('[data-toggle="popover"]').popover();
    document.getElementById('panier').setAttribute('data-content', panierString);
}


