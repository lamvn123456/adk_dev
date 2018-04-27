using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
namespace menu
{
    public class MenuController : MonoBehaviour
    {

        /*  
        * Move to Newgame scene
        */
        public void NewGame()
        {
            SceneManager.LoadScene("NewGame");
        }

        /*
        * Move to LoadGame scene
        */
        public void LoadGame()
        {
            SceneManager.LoadScene("LoadGame");
        }

        /*
        * Move to Customization Scene
        */
        public void CustomizeGame()
        {
            SceneManager.LoadScene("CustomizeGame");
        }

        /*  
        * Quit game
        */
        public void Quit()
        {
            Application.Quit();
        }
        

    }
}