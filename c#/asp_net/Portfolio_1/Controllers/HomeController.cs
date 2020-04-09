using Microsoft.AspNetCore.Mvc;

namespace Portfolio_1
{
    public class HomeController : Controller
    {
        // Requests
        //localhost:5000/
        [Route("")]
        [HttpGet]
        public string Index()
        {
            return "This is my Index!";
        }

        //localhost:5000/hello
        [Route("hello")]
        [HttpGet]
        public string Hello()
        {
            return "Hi Again!";
        }
        
        //localhost:5000/projects
        [Route("projects")]
        [HttpGet]
        public string projects()
        {
            return "These are my projects";
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