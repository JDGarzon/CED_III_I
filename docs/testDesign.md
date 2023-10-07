# Diseño de pruebas
| Prueba                   | Descripción                                          | Casos de Prueba y Resultados Esperados                                    |
|--------------------------|------------------------------------------------------|--------------------------------------------------------------------------|
| test_dialogos            | Prueba de la función `dialogos`                     | - Llamar a `novel.dialogos(0, "1")` debería devolver 'Tu hija ha ...'   |
| test_validate_name       | Prueba de la función `validate_name`                | - Llamar a `novel.validate_name('Nombre')` debería devolver True        |
|                          |                                                      | - Llamar a `novel.validate_name('')` debería devolver False             |
| test_translate           | Prueba de la función `translate`                    | - Llamar a `novel.translate("1", "")` debería devolver '1'              |
|                          |                                                      | - Llamar a `novel.translate("#$%", "Nombre")` debería devolver 'Nombre' |
|                          |                                                      | - Llamar a `novel.translate("Soy #$% y voy a mi casa", "Alguien")`    |
|                          |                                                      |   debería devolver 'Soy Alguien y voy a mi casa'                        |
| test_advance             | Prueba de la función `advance`                      | - Llamar a `novel.advance("a", current)` debería devolver 'Decides ...' |
|                          |                                                      | - Llamar a `novel.advance("b", current)` debería devolver 'Decides ...'|
|                          |                                                      | - Llamar a `novel.advance("a", current)` y verificar que no sea igual  |
|                          |                                                      |   a 'Decides ignorar el desorden ...' debería devolver False           |
