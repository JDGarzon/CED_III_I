# Diseño de pruebas
| Prueba           | Descripción                             | Casos de Prueba y Resultados Esperados    |
|------------------|-----------------------------------------|------------------------------------------|
| test_dialogos    | Verifica la función 'dialogos' del      |                                          |
|                  | módulo 'novel'.                        |                                          |
|------------------|-----------------------------------------|------------------------------------------|
|                  |                                         |                                          |
| Caso de Prueba 1 | Llamada a 'novel.dialogos(0, "1")'      | Debe devolver una cadena que contiene el |
|                  |                                         | diálogo.                                 |
|                  |                                         |                                          |
|------------------|-----------------------------------------|------------------------------------------|
| test_validate_name | Verifica la función 'validate_name' del |                                          |
|                  | módulo 'novel' que valida un nombre.    |                                          |
|------------------|-----------------------------------------|------------------------------------------|
|                  |                                         |                                          |
| Caso de Prueba 1 | Llamada a 'novel.validate_name('Nombre')' | Debe retornar 'True' ya que 'Nombre' es |
|                  |                                         | un nombre válido.                        |
|                  |                                         |                                          |
| Caso de Prueba 2 | Llamada a 'novel.validate_name('')'      | Debe retornar 'False' ya que la cadena  |
|                  |                                         | está vacía.                              |
|                  |                                         |                                          |
|------------------|-----------------------------------------|------------------------------------------|
| test_validate_answer | Verifica la función 'validate_answer'  |                                          |
|                  | del módulo 'novel' que valida una       |                                          |
|                  | respuesta.                               |                                          |
|------------------|-----------------------------------------|------------------------------------------|
|                  |                                         |                                          |
| Caso de Prueba 1 | Llamada a 'novel.validate_answer('a')'  | Debe retornar 'True' ya que 'a' es una  |
|                  |                                         | respuesta válida.                        |
|                  |                                         |                                          |
| Caso de Prueba 2 | Llamada a 'novel.validate_answer('b')'  | Debe retornar 'True' ya que 'b' es una  |
|                  |                                         | respuesta válida.                        |
|                  |                                         |                                          |
| Caso de Prueba 3 | Llamada a 'novel.validate_answer('')'   | Debe retornar 'False' ya que la cadena  |
|                  |                                         | está vacía.                              |
|                  |                                         |                                          |
| Caso de Prueba 4 | Llamada a 'novel.validate_answer('c')'  | Debe retornar 'False' ya que 'c' no es  |
|                  |                                         | una respuesta válida.                   |
|                  |                                         |                                          |
| Caso de Prueba 5 | Llamada a 'novel.validate_answer('aa')' | Debe retornar 'False' ya que 'aa' no es |
|                  |                                         | una respuesta válida.                   |
|                  |                                         |                                          |
| Caso de Prueba 6 | Llamada a 'novel.validate_answer('ab')' | Debe retornar 'False' ya que 'ab' no es |
|                  |                                         | una respuesta válida.                   |
|                  |                                         |                                          |
|------------------|-----------------------------------------|------------------------------------------|
| test_translate   | Verifica la función 'translate' del     |                                          |
|                  | módulo 'novel' que realiza una         |                                          |
|                  | traducción de una cadena.               |                                          |
|------------------|-----------------------------------------|------------------------------------------|
|                  |                                         |                                          |
| Caso de Prueba 1 | Llamada a 'novel.translate("1", "")'   | Debe retornar '1' ya que no hay         |
|                  |                                         | caracteres para reemplazar.             |
|                  |                                         |                                          |
| Caso de Prueba 2 | Llamada a 'novel.translate("#$%",       | Debe retornar 'Nombre' ya que la cadena |
|                  | "Nombre")'                              | de reemplazo no contiene caracteres     |
|                  |                                         | especiales.                              |
|                  |                                         |                                          |
| Caso de Prueba 3 | Llamada a 'novel.translate("Soy #$% y  | Debe retornar 'Soy Alguien y voy a mi  |
|                  | voy a mi casa", "Alguien")'            | casa' después de reemplazar '#$%' con  |
|                  |                                         | 'Alguien'.                               |
|                  |                                         |                                          |
