# Scan and Crop
## But
Numériser automatiquement une photo (en format A4) et la découper pour ne retenir que sa partie utile.
Les photos générées auront pour préfixe celui qu'on leur donne, comme nom la date et l'heure et comme suffixe '_cropped'. 
> **Warning**  
> le lancement du scan se fait en commande OS. Actuellement seuls les scanners HP sont configurés. 
## Fichiers

| Fichier| Description-Fonction
| -------- | -------- |
| crop.py   | Découpage de l'image en supprimant les tours en blanc. Est utilisé dans Scrop.py et peut être  utilisé en lancement avec en paramètre le fichier à découper|
| BA.jpg    | Image en exemple pour être découpée|
| crop.sh   | Peut être utilisé dans les scripts du navigateur pour découper une image existante - à adapter |
| Scrop.py    | Interface utilisateur. On choisit le préfixe et le répertoire de sauvegarde (valable et unique toute les session). On peut boucler sur les scans. |
## Technique
Par simplicité on utilise tkinter pour l'interface graphique; ainsi, à priori, aucune libtrairie python n'est à installer.
