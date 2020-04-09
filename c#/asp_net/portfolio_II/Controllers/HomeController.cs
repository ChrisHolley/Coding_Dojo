using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

namespace Portfolio_1
{
    public class HomeController : Controller
    {
        // Requests
        //localhost:5000/
        [Route("")]
        [HttpGet]
        public ViewResult aboutMe() //ViewResult is return type for any methods that ONLY render an html page will look for HiThere.cshtml
        {
            // Views/Home/HiThere.cshtml
            // Views/Shared/HiThere.cshtml
            
            return View();
        }

        //localhost:5000/projects
        [Route("projects")]
        [HttpGet]
        public ViewResult projects()
        {
            return View();
        }
        
        //localhost:5000/contactMe
        [Route("contactMe")]
        [HttpGet]
        public ViewResult contactMe()
        {
            return View();
        }
        
        //localhost:5000/contact
        [Route("contact")]
        [HttpGet]
        public string contact()
        {
            return "This is my Contact!";
        }

        // localhost:5000/users/???
        [HttpGet("users/{username}/{location}")]
        public string HelloUser(string username, string location)
        {
            if(location == "Chicago")
                return $"Hello {username}, from {location}. Go Bears!";
            return $"Hello {username}, from {location}";
        }

    }
}