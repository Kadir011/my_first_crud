(function () {
    const btnEliminar = document.querySelectorAll(".btnEliminar") 
    btnEliminar.forEach( btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro que desea eliminar el Libro?');
            if (!confirmacion) {
                e.preventDefault(); 
            } 
        }); 
    });
})();

(function () {
    const btnEditar = document.querySelectorAll(".btnEditar") 
    btnEditar.forEach( btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro que desea actulizar el Libro?');
            if (!confirmacion) {
                e.preventDefault(); 
            } 
        }); 
    });
})();

(function () {
    const btnCancelar = document.querySelectorAll(".btnCancelar") 
    btnCancelar.forEach( btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro que desea cancelar?');
            if (!confirmacion) {
                e.preventDefault(); 
            } 
        }); 
    });
})();


(function () {
    const btnAgregar = document.querySelectorAll(".btnAgregar") 
    btnAgregar.forEach( btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Desea agregar el libro?');
            if (!confirmacion) {
                e.preventDefault(); 
            } 
        }); 
    });
})(); 

(function () {
    const btnCerrar = document.querySelectorAll(".btnCerrar") 
    btnCerrar.forEach( btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Desea cerrar sesión?');
            if (!confirmacion) {
                e.preventDefault(); 
            } 
        }); 
    });
})(); 










