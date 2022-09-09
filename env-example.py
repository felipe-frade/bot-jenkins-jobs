USER_JENKINS = ''
PASS_JENKINS = ''

ID_JENKINS = 1
URL_LOGIN_JENKINS = ''

EL_REPOS = '[itemprop="name codeRepository"]'

DB_HOST = ''''''
DB_DATABASE = ''''''
DB_USER = ''''''
DB_PASS = ''''''

# Estrutura das tabelas
"""
  CREATE TABLE IF NOT EXISTS `ctrl_jenkins` (
    `id_jenkins` int(11) NOT NULL AUTO_INCREMENT,
    `link_jenkins` text,
    PRIMARY KEY (`id_jenkins`)
  ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
  
  CREATE TABLE IF NOT EXISTS `ctrl_jenkins_jobs` (
    `id_job` int(11) NOT NULL AUTO_INCREMENT,
    `nome_job` varchar(100) NOT NULL DEFAULT '',
    `jenkins` int(11) NOT NULL DEFAULT '0',
    `tipo_job` enum('F','P') NOT NULL DEFAULT 'F' COMMENT 'F - freestyle, P - pipeline',
    `destruir_build` enum('S','N') NOT NULL DEFAULT 'N',
    `ativo` enum('S','N') DEFAULT 'S',
    PRIMARY KEY (`id_job`),
    UNIQUE KEY `JJ` (`nome_job`,`jenkins`,`ativo`),
    KEY `FK_jenkins_ctrl_jenkins` (`jenkins`),
    CONSTRAINT `FK_jenkins_ctrl_jenkins` FOREIGN KEY (`jenkins`) REFERENCES `ctrl_jenkins` (`id_jenkins`) ON DELETE CASCADE ON UPDATE CASCADE
  ) ENGINE=InnoDB AUTO_INCREMENT=122 DEFAULT CHARSET=utf8;
"""