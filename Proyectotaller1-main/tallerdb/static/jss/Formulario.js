function validateForm(event) {
    event.preventDefault(); // Evitar el envío del formulario por defecto

    // Obtener los valores del formulario
    var rut = document.getElementById('rut').value;
    var nombre = document.getElementById('nombre').value;
    var apellido_paterno = document.getElementById('apellido_paterno').value;
    var apellido_materno = document.getElementById('apellido_materno').value;
    var telefono = document.getElementById('telefono').value;
    var email = document.getElementById('email').value;
    var direccion = document.getElementById('direccion').value;
    var activo = document.getElementById('activo').value;
    

    // Realizar las validaciones
    var errors = [];
    if (rut === '') {
      errors.push('El RUT es obligatorio.');
    } else {
      // Validar formato de RUT usando una expresión regular simple
      var rutPattern = /^[0-9]{1,2}\.[0-9]{3}\.[0-9]{3}-[0-9kK]{1}$/;
      if (!rutPattern.test(rut)) {
        errors.push('El RUT ingresado no es válido , rut debe tener este formato xx.xxx.xxx-x.');
      }
    }

    if (nombre === '') {
      errors.push('El nombre es obligatorio.');
    }

    if (apellido_paterno === '') {
      errors.push('El apellido es obligatorio.');
    }

    if (apellido_materno === '') {
      errors.push('El apellido es obligatorio.');
    }

    if (telefono === '') {
      errors.push('El número telefónico es obligatorio.');
    } else {
      // Validar formato de número telefónico usando una expresión regular simple
      var telefonoPattern = /^[0-9]{9}$/;
      if (!telefonoPattern.test(telefono)) {
        errors.push('El número telefónico ingresado no es válido , debe tener 9 digitos .');
      }
    }

    if (email === '') {
      errors.push('El correo electrónico es obligatorio.');
    } else {
      // Validar formato de correo electrónico usando una expresión regular simple
      var correoPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!correoPattern.test(correo)) {
        errors.push('El correo electrónico ingresado no es válido.');
      }
    }
    if (direccion === '') {
      errors.push('la direccion es obligatoria');
    }
    if (activo === '') {
      errors.push('la direccion es obligatoria');
    }
    // Mostrar los errores o enviar el formulario
    if (errors.length > 0) {
      var errorMessage = 'Error:\n\n' + errors.join('\n');
      alert(errorMessage);
    } else {
      alert('Enviado con éxito.');
      document.getElementById('myForm').reset(); // Reiniciar el formulario después de enviarlo
    }
  }