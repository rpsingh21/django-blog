  var app = angular.module('post', []);
  app.controller('comments', function($scope, $http) {
      $http({
          method : "GET",
          url : "/api/comments/1/"
      }).then(function mySuccess(response) {
          $scope.allcomments = response.data;
          console.log($scope.allcomments)
      }, function myError(response) {
          $scope.myWelcome = response.statusText;
      });
  });