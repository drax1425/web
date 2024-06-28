function confirmarDelete(id){
    Swal.fire({
        title: "Estas seguro de que deseas eliminar ?",
        text: "Los cambios son ireversibles!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si,eliminar!"
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire({
            title: "Eliminado!",
            text: "Periodista eliminado correctamente.",
            icon: "success"
          }).then(function(){
            window.location.href="/empleados/delete/"+id+"/";
          })
        }
      });

}