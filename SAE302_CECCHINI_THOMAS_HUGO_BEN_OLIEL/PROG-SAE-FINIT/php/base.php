<?php
	header('Content-Type: application/json; charset=utf-8');
    // Connexion
    $conn = new mysqli("mysql.pedaweb.univ-amu.fr", "c21220018", "wsCVnewDzfp7FYv", "c21220018");

    // Error handler
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Obtenir la requête dans l'url
  	    $method = $_SERVER['REQUEST_METHOD'];

    $input = null;
    switch($method) {
        case 'PUT':
            $input = json_decode(file_get_contents('php://input'),true);
            break;
        case 'DELETE':
            $input = json_decode(file_get_contents('php://input'),true);
            break;
        case 'GET':
            $input = $_GET;
            break;
        case 'POST':
            $input = json_decode(file_get_contents('php://input'),true);
            break;

    }

    $table = $input["table"];
    $key = isset($input["id"]) ? $input["id"] : null;

	
    // Découpage du chemin
    $columns = preg_replace('/[^a-z0-9_]+/i','',array_keys($input));
    $values = array_map(function ($value) use ($conn) {
        if ($value===null) return null;
        return mysqli_real_escape_string($conn,(string)$value);
    },array_values($input));

    // Construction de la requête
    $set = '';
    array_shift($columns); // On enlève l'index "table" qui nous est inutile
    array_shift($values); // Et la valeur de l'index table

    for ($i=0;$i<count($columns);$i++) {
        $set.=($i>0?',':'').'`'.$columns[$i].'`=';
        if($columns[$i] == "password") {
            $set.=($values[$i]===null?'NULL':'"'.password_hash($values[$i], PASSWORD_DEFAULT).'"');
        } else {
            $set.=($values[$i]===null?'NULL':'"'.$values[$i].'"');
        }
    }

    // Switch selon l'url
    switch ($method) {
        case 'GET':
            if($table == "etudiants"){
                $sql = "select * from `$table`".($key?" WHERE id=$key":'');
            }else if($table == "matieres"){
                $sql = "select * from `$table`".($key?" WHERE id_etu=$key":'');
            }else if($table == "profile"){
                $sql = "select * from `$table`".($key?" WHERE id_etu=$key":'');
            }
            break;
        case 'PUT':
            if($table == "etudiants"){
                $sql = "update `$table` set $set where id=$key";
            }else if($table == "matieres"){
                $sql = "update `$table` set $set where id_etu=$key";
            }else if($table == "profile"){
                $sql = "update `$table` set $set where id_etu=$key";
            }
            break;
        case 'POST':
            if($table == "etudiants"){
                $sql = "insert into `$table` set $set";
            }else if($table == "matieres"){
                $sql = "insert into `$table` set $set";
            }else if($table == "profile"){
                $sql = "insert into $table set $set";
            }
            break;
        case 'DELETE':
            if($table == "etudiants"){
                $sql = "delete from $table where id=$key";
            }else if($table == "matieres"){
                $sql = "delete from $table where id_etu=$key";
            }else if($table == "profile"){
                $sql = "delete from $table where id_etu=$key";
            }
            break;
    }
	
    // éxecution de la requête
    $result = mysqli_query($conn,$sql);

    // Error handler
    if (!$result) {
        http_response_code(404);
        die(mysqli_error());
    }

    // Print result
    if ($method == 'GET') {
        if (!$key) echo '[';
        for ($i=0;$i<mysqli_num_rows($result);$i++) {
            echo ($i>0?',':'').json_encode(mysqli_fetch_object($result));
        }
        if (!$key) echo ']';
    } elseif ($method == 'POST') {
        echo mysqli_insert_id($conn);
    } else {
        echo mysqli_affected_rows($conn);
    }

    // close mysql connection
    $conn->close();
?>