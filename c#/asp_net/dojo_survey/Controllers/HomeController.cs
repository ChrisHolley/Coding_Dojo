using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

namespace dojo_survey
{
    public class HomeController : Controller
    {
        // Requests
        //localhost:5000/
        [Route("")]
        [HttpGet]
        public ViewResult index() //ViewResult is return type for any methods that ONLY render an html page will look for HiThere.cshtml
        {
            // Views/Home/HiThere.cshtml
            // Views/Shared/HiThere.cshtml
            
            return View();
        }

        //localhost:5000/result
        [Route("result")]
        [HttpGet]
        public IActionResult result()
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