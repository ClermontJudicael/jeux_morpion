![image](https://github.com/ClermontJudicael/jeux_morpion/assets/135115381/604efbc6-7120-4f61-8740-a437df898c88)# Morpion game

A school project made by Clermont Judicaël, @Miantsa7 and more

# Game overview
### 3x3
![3x3](https://github.com/ClermontJudicael/jeux_morpion/assets/135115381/9e747ff1-63d8-461a-9de3-b188cc68e21f)

### 6x6
![6x6](https://github.com/ClermontJudicael/jeux_morpion/assets/135115381/ed2ecf17-9522-46c9-a774-176b1fda3995)

## Install requirements:

<!DOCTYPE html>
<html>
<head>
  <title>README</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.8/clipboard.min.js"></script>
  <style>
    .btn {
      border: none;
      background: #007bff;
      color: #fff;
      padding: 5px 10px;
      cursor: pointer;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <pre><code id="commande">pip install -r requirements.txt</code></pre>
  <button class="btn" data-clipboard-target="#commande">Copier</button>

  <script>
    var clipboard = new ClipboardJS('.btn');

    clipboard.on('success', function(e) {
      e.clearSelection();
      console.log('Copié !');
    });

    clipboard.on('error', function(e) {
      console.error('Échec de la copie : ', e);
    });
  </script>
</body>
</html>

