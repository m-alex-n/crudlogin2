$(".delete").click(function (e) {
  e.preventDefault();

  var self = $(this);
  console.log(self.data("title"));

  Swal.fire({
    title: "Are you sure?",
    text: "You won't be able to revert this!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Yes, delete it!",
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire("Deleted!", "Your file has been deleted.", "success");
      //location.href = self.attr(".tabledata");
      //   $(".tabledata").load(location.href + " .tabledata");
    }
  });
});
