using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using System.IO;

namespace NewGame
{
    public class NewGameController : MonoBehaviour
    {
        public Dropdown asianRegionDropdown;
        public Dropdown euroRegionDropdown;
        public Dropdown southAmericaDropdown;
        public Dropdown northAmericaDropdown;
        public Dropdown databaseDropdown;

        void Start()
        {
            List<string> databaseOptions = new List<string>();
            DirectoryInfo databaseDir = new DirectoryInfo("Database");
            FileInfo[] databaseFiles = databaseDir.GetFiles("*.dbem"); //Getting Text files
            foreach (FileInfo file in databaseFiles)
            {
                print(file.Name);
                databaseOptions.Add(file.Name);
            }
            print(databaseOptions[0]);
            databaseDropdown.AddOptions(databaseOptions);
        }
    }
}
